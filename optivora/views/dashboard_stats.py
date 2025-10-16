from django.db.models import Count
from django.utils.timezone import now
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from users.models import User, Role  # yo'lingizga moslab o'zgartiring
from optivora.models import (
    Industry, Service, EquipmentCategory, Partner, Project, Inquiry, NewsPost
)

@api_view(["GET"])
@permission_classes([AllowAny])  # kerak bo'lsa IsAuthenticated ga almashtiring
def dashboard_stats(request):
    # --- Users by role ---
    # FK: User.role -> Role, related_name='role_user'
    roles_qs = Role.objects.annotate(user_count=Count('role_user'))
    users_by_role = [
        {
            "id": r.id,
            "name": r.name,                 # Group.name (Role meros olgan)
            "description": r.description,
            "count": r.user_count,
        }
        for r in roles_qs
    ]

    # Gender bo‘yicha ham foydali bo‘lishi mumkin (ixtiyoriy)
    gender_counts_map = {}
    for row in User.objects.values('gender').annotate(count=Count('id')):
        key = row['gender'] or "unknown"
        gender_counts_map[key] = row['count']

    # --- Catalog counts ---
    industries_total = Industry.objects.count()
    services_total = Service.objects.count()
    equipment_categories_total = EquipmentCategory.objects.count()

    # Partners total + by category (label bilan)
    partners_total = Partner.objects.count()
    category_label = dict(Partner.CATEGORY.choices) if hasattr(Partner, "CATEGORY") else {}
    partners_by_category = []
    for row in Partner.objects.values('category').annotate(count=Count('id')).order_by():
        code = row['category'] or "unknown"
        partners_by_category.append({
            "code": code,
            "label": category_label.get(code, "Unknown"),
            "count": row['count']
        })

    # --- Projects ---
    projects_total = Project.objects.count()
    projects_featured = Project.objects.filter(is_featured=True).count()

    # --- Inquiries ---
    inquiries_total = Inquiry.objects.count()
    status_label = dict(Inquiry.STATUS.choices) if hasattr(Inquiry, "STATUS") else {}
    inquiries_by_status = []
    for row in Inquiry.objects.values('status').annotate(count=Count('id')).order_by():
        code = row['status'] or "unknown"
        inquiries_by_status.append({
            "code": code,
            "label": status_label.get(code, "Unknown"),
            "count": row['count']
        })

    # --- News ---
    news_total = NewsPost.objects.count()
    news_published = NewsPost.objects.filter(status=NewsPost.STATUS.PUBLISHED).count() if hasattr(NewsPost, "STATUS") else 0
    news_draft = NewsPost.objects.filter(status=NewsPost.STATUS.DRAFT).count() if hasattr(NewsPost, "STATUS") else 0

    data = {
        "generated_at": now().isoformat(),
        "users": {
            "total": User.objects.count(),
            "by_role": users_by_role,
            "by_gender": gender_counts_map,  # {"male": n, "female": m, "unknown": k}
        },
        "catalog": {
            "industries": industries_total,
            "services": services_total,
            "equipment_categories": equipment_categories_total,
            "partners": {
                "total": partners_total,
                "by_category": partners_by_category
            }
        },
        "projects": {
            "total": projects_total,
            "featured": projects_featured
        },
        "inquiries": {
            "total": inquiries_total,
            "by_status": inquiries_by_status
        },
        "news": {
            "total": news_total,
            "published": news_published,
            "draft": news_draft
        }
    }
    return Response(data)
