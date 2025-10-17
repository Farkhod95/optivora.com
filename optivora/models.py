# apps/website/models.py
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator, MinValueValidator, MaxValueValidator

from directory.models import Region, District, Country
from restapp.models import BaseModel


class CompanyProfile(BaseModel):
    """Kompaniya profili: footer, Contact sahifasi va umumiy ma’lumotlar uchun bitta yozuv."""
    name = models.CharField(_('Kompaniya nomi'), max_length=150, default='Optivora', null=True, blank=True, help_text=_('Kompaniya to‘liq nomi'))  # Masalan: Optivora
    logo = models.ImageField(upload_to='company/logo/%Y/%m/', null=True, blank=True, verbose_name=_('Logo'), help_text=_('Kompaniya logotipi (ixtiyoriy)'))  # PNG/SVG/JPG
    email = models.EmailField(_('Email'), max_length=254, null=True, blank=True, help_text=_('Rasmiy aloqa e-pochtasi'))  # info@...
    phone = models.CharField(_('Telefon'), max_length=64, null=True, blank=True, help_text=_('Aloqa uchun telefon raqami'))  # +998...
    address = models.CharField(_('Manzil'), max_length=255, null=True, blank=True, help_text=_('Ofis manzili, shahar va mamlakat bilan'))  # Tashkent, Uzbekistan
    business_hours = models.CharField(_('Ish vaqti'), max_length=255, null=True, blank=True, help_text=_('Ish kunlari va ish soatlari (masalan: Du-Ju 09:00–18:00)'))  # Matn ko‘rinishida
    title = models.CharField(_('Kompaniya sarlavhasi'), max_length=150, default='Optivora',
                            help_text=_('Kompaniya sarlavhasi'))  # Masalan: Optivora
    description = models.TextField(_('Tavsif'), null=True, blank=True,
                                   help_text=_('Kompaniya haqida batafsil tavsif (ixtiyoriy)'))  # SEO/Detail
    file = models.FileField(upload_to='company/%Y/%m/', null=True, validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx'])], help_text=_('Yuklanadigan fayl'))  # Fayl kontenti
    years_experience = models.CharField(_('Yillik tajriba'), max_length=64, null=True, blank=True,
                             help_text=_('Yillik tajriba'))  # +998...
    equipment_categories = models.CharField(_('Uskunalar toifalari'), max_length=64, null=True, blank=True,
                             help_text=_('Uskunalar toifalari'))  # +998...
    projects_supported = models.CharField(_('Qo\'llab-quvvatlanadigan loyihalar'), max_length=64, null=True, blank=True,
                             help_text=_('Qo\'llab-quvvatlanadigan loyihalar'))  # +998...
    international_partners = models.CharField(_('Xalqaro hamkorlar'), max_length=64, null=True, blank=True,
                             help_text=_('Xalqaro hamkorlar'))  # +998...

    class Meta:
        verbose_name = _('Kompaniya profili')
        verbose_name_plural = _('Kompaniya profili')

    def __str__(self):
        return self.name


class Industry(BaseModel):
    """Sektorlar (Industries We Serve): Power Generation, Water & Wastewater va h.k."""
    name = models.CharField(_('Nomi'), max_length=120, null=True, blank=True, unique=True, help_text=_('Sektor nomi (masalan: Power Generation)'))  # Unikal nom
    slug = models.SlugField(_('Slug'), max_length=140, unique=True, null=True, blank=True, help_text=_('URL uchun unikal identifikator (kichik lotin, tire)'))  # URL-friendly
    short_description = models.CharField(_('Qisqa tavsif'), max_length=255, null=True, blank=True, help_text=_('Sektor bo‘yicha qisqa bir jumla'))  # Kartochka uchun
    description = models.TextField(_('Tavsif'), null=True, blank=True, help_text=_('Sektor haqida batafsil tavsif (ixtiyoriy)'))  # SEO/Detail
    icon = models.ImageField(upload_to='industries/icons/%Y/%m/', null=True, blank=True, help_text=_('Sektor ikonkasi (ixtiyoriy)'))  # UI ikona
    order_index = models.PositiveIntegerField(unique=True, verbose_name=_('Tartib'), help_text=_('Chop etishda tartib (kichik son – oldinda)'))  # Sortlash

    class Meta:
        verbose_name = _('Sektor')
        verbose_name_plural = _('Sektorlar')

    def __str__(self):
        return self.name


class EquipmentCategory(BaseModel):
    """Uskuna toifalari: Control & Automation, Rotating Machinery, Safety & Monitoring, va b."""
    name = models.CharField(_('Nomi'), max_length=120, null=True, blank=True, unique=True, help_text=_('Uskuna kategoriyasi nomi (masalan: Control & Automation)'))  # Unikal nom
    slug = models.SlugField(_('Slug'), max_length=140, unique=True, help_text=_('URL uchun unikal identifikator'))  # URL-friendly
    description = models.TextField(_('Tavsif'), null=True, blank=True, help_text=_('Kategoriyaga oid batafsil tavsif (ixtiyoriy)'))  # SEO/Detail
    order_index = models.PositiveIntegerField(unique=True, verbose_name=_('Tartib'), help_text=_('Chop etish tartibi'))  # Sortlash

    class Meta:
        verbose_name = _('Uskuna kategoriyasi')
        verbose_name_plural = _('Uskuna kategoriyalari')

    def __str__(self):
        return self.name


class Service(BaseModel):
    """Xizmatlar (Solutions & Services): Equipment Supply, Technical Coordination va h.k."""
    name = models.CharField(_('Xizmat nomi'), null=True, blank=True, max_length=150, unique=True, help_text=_('Xizmatning to‘liq nomi (masalan: Equipment Supply & Procurement)'))  # Unikal nom
    slug = models.SlugField(_('Slug'), max_length=160, unique=True, null=True, blank=True, help_text=_('URL uchun unikal identifikator'))  # URL-friendly
    short_description = models.CharField(_('Qisqa tavsif'), max_length=255, null=True, blank=True, help_text=_('Xizmat bo‘yicha qisqacha jumla'))  # Kartochka qisqacha matn
    description = models.TextField(_('Batafsil tavsif'), null=True, blank=True, help_text=_('Xizmat tafsilotlari (ixtiyoriy)'))  # Batafsil matn
    icon = models.ImageField(upload_to='services/icons/%Y/%m/', null=True, blank=True, help_text=_('Xizmat ikonkasi (ixtiyoriy)'))  # UI ikona
    industries = models.ManyToManyField(Industry, related_name='services', blank=True, verbose_name=_('Sektorlar'), help_text=_('Xizmat qamrab oladigan sektorlar (ixtiyoriy)'))  # Aloqa: sektorlar
    equipment_categories = models.ManyToManyField(EquipmentCategory, related_name='services', blank=True, verbose_name=_('Uskuna kategoriyalari'), help_text=_('Xizmatga tegishli uskunalar toifalari (ixtiyoriy)'))  # Aloqa: uskunalar
    order_index = models.PositiveIntegerField(unique=True, verbose_name=_('Tartib'), help_text=_('Chop etish tartibi'))  # Sortlash

    class Meta:
        verbose_name = _('Xizmat')
        verbose_name_plural = _('Xizmatlar')

    def __str__(self):
        return self.name


class Partner(BaseModel):
    """Hamkor/Manufacturerlar: bo‘limlar bo‘yicha guruhlanadi (logo grid)."""
    class CATEGORY(models.TextChoices):
        POWER_CONTROL = 'power_control', _('Power & Control Systems')
        ROTATING = 'rotating', _('Rotating Equipment & Pumps')
        SPECIALIZED = 'specialized', _('Specialized Systems')
        SAFETY_MONITORING = 'safety_monitoring', _('Safety & Monitoring')
        ELECTRICAL_POWER = 'electrical_power', _('Electrical & Power Components')

    name = models.CharField(_('Nomi'), max_length=160, null=True, blank=True, unique=True, help_text=_('Hamkor/manufacturer nomi'))  # Masalan: Statron
    category = models.CharField(_('Kategoriya'), max_length=40, null=True, blank=True, choices=CATEGORY.choices, help_text=_('Hamkor toifasi'))  # Tanlov: bo‘lim
    logo = models.ImageField(upload_to='partners/logos/%Y/%m/', null=True, blank=True, help_text=_('Hamkor logotipi (ixtiyoriy)'))  # PNG/JPG
    website = models.URLField(_('Veb-sayt'), null=True, blank=True, help_text=_('Rasmiy veb-sayt manzili (ixtiyoriy)'))  # https://...
    description = models.TextField(_('Qisqa tavsif'), null=True, blank=True, help_text=_('Hamkor haqida qisqa tavsif (ixtiyoriy)'))  # Katalog matni
    industries = models.ManyToManyField(Industry, related_name='partners', blank=True, verbose_name=_('Sektorlar'), help_text=_('Hamkor qamrab oladigan sektorlar (ixtiyoriy)'))  # Aloqa: sektorlar
    equipment_categories = models.ManyToManyField(EquipmentCategory, related_name='partners', blank=True, verbose_name=_('Uskuna kategoriyalari'), help_text=_('Hamkor taqdim etadigan uskunalar toifalari (ixtiyoriy)'))  # Aloqa: uskunalar
    order_index = models.PositiveIntegerField(unique=True, verbose_name=_('Tartib'), help_text=_('Chop etish tartibi'))  # Sortlash

    class Meta:
        verbose_name = _('Hamkor')
        verbose_name_plural = _('Hamkorlar')

    def __str__(self):
        return self.name


class Project(BaseModel):
    """Loyihalar/References: Projects & Experience sahifasi uchun karta/grid ko‘rinishidagi yozuvlar."""
    title = models.CharField(_('Loyiha nomi'), max_length=200, null=True, blank=True, help_text=_('Loyiha to‘liq nomi'))  # Karta sarlavhasi
    slug = models.SlugField(_('Slug'), max_length=220, unique=True, null=True, blank=True, help_text=_('URL uchun unikal identifikator'))  # URL-friendly
    country = models.ForeignKey(Country, null=True, blank=True, on_delete=models.CASCADE, related_name='project_country',
                               verbose_name=_('Mamlakat'), help_text=_('Qaysi loyihaga tegishli deliverable'))
    region = models.ForeignKey(Region, null=True, blank=True, on_delete=models.CASCADE, related_name='project_region',
                                verbose_name=_('Viloyat'), help_text=_('Qaysi loyihaga tegishli deliverable'))
    # location_city = models.CharField(_('Shahar'), max_length=120, null=True, blank=True, help_text=_('Loyiha shahri (ixtiyoriy)'))  # Masalan: Tashkent
    # location_region = models.CharField(_('Viloyat/Region'), max_length=120, null=True, blank=True, help_text=_('Loyiha joylashuvi (ixtiyoriy)'))  # Masalan: Tashkent Region
    district = models.ForeignKey(District, null=True, blank=True, on_delete=models.CASCADE, related_name='project_district',
                               verbose_name=_('Tuman'), help_text=_('Qaysi loyihaga tegishli deliverable'))
    year = models.PositiveSmallIntegerField(_('Yil'), validators=[MinValueValidator(1990), MaxValueValidator(2100)], null=True, blank=True, help_text=_('Loyiha yilini kiriting (masalan: 2025)'))  # Filtr/ko‘rsatish uchun
    scope = models.CharField(_('Qamrov (scope)'), max_length=255, null=True, blank=True, help_text=_('Masalan: Supply of advanced power electronics and control systems'))  # Qisqacha scope
    summary = models.TextField(_('Qisqa izoh'), null=True, blank=True, help_text=_('Loyiha haqida qisqa sharh (ixtiyoriy)'))  # Batafsil
    featured_image = models.ImageField(upload_to='projects/featured/%Y/%m/', null=True, blank=True, help_text=_('Asosiy rasm (ixtiyoriy)'))  # Karta rasmi
    industries = models.ManyToManyField(Industry, related_name='projects', blank=True, verbose_name=_('Sektorlar'), help_text=_('Loyiha tegishli sektorlar (ixtiyoriy)'))  # Aloqa: sektor
    equipment_categories = models.ManyToManyField(EquipmentCategory, related_name='projects', blank=True, verbose_name=_('Uskuna kategoriyalari'), help_text=_('Loyihadagi uskunalar toifalari (ixtiyoriy)'))  # Aloqa: uskunalar
    partners = models.ManyToManyField(Partner, related_name='projects', blank=True, verbose_name=_('Hamkorlar'), help_text=_('Loyihada ishtirok etgan hamkorlar (ixtiyoriy)'))  # Aloqa: hamkor
    is_featured = models.BooleanField(default=False, verbose_name=_('Tavsiya etilgan'), null=True, blank=True, help_text=_('Bosh sahifada yoki ro‘yxat tepasida ko‘rsatish'))  # Flag
    order_index = models.PositiveIntegerField(unique=True, verbose_name=_('Tartib'), help_text=_('Chop etish tartibi'))  # Sortlash

    class Meta:
        verbose_name = _('Loyiha')
        verbose_name_plural = _('Loyihalar')

    def __str__(self):
        return f"{self.title} ({self.year})"


class ProjectDeliverable(BaseModel):
    """Loyiha bo‘yicha ‘Key Deliverables’ elementlari (bulleted ro‘yxat)."""
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='deliverables', verbose_name=_('Loyiha'), help_text=_('Qaysi loyihaga tegishli deliverable'))  # FK: Project
    name = models.CharField(_('Yetkazib beriladigan pozitsiya'), max_length=200, null=True, blank=True, help_text=_('Deliverable nomi (masalan: High-capacity inverter systems)'))  # Matn elementi

    class Meta:
        verbose_name = _('Loyiha deliverabli')
        verbose_name_plural = _('Loyiha deliverabllari')

    def __str__(self):
        return self.name


class ProjectImage(BaseModel):
    """Loyiha galereyasi rasmlari: lightbox/modal uchun tartib bilan."""
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images', verbose_name=_('Loyiha'), help_text=_('Rasm tegishli loyihasi'))  # FK: Project
    image = models.ImageField(upload_to='projects/gallery/%Y/%m/', null=True, blank=True, help_text=_('Loyiha galereyasi rasmi'))  # JPG/PNG
    caption = models.CharField(_('Sarlavha'), max_length=200, null=True, blank=True, help_text=_('Rasm izohi (ixtiyoriy)'))  # Caption
    order_index = models.PositiveIntegerField( unique=True, verbose_name=_('Tartib'), help_text=_('Galereyada ko‘rinish tartibi'))  # Tartib

    class Meta:
        verbose_name = _('Loyiha rasmi')
        verbose_name_plural = _('Loyiha rasmlari')

    def __str__(self):
        return f"{self.project.title} - {self.id}"


class StatItem(BaseModel):
    """‘By The Numbers’ bo‘limidagi statistik ko‘rsatkichlar (4 ta blok)."""
    label = models.CharField(_('Nomi'), max_length=200, null=True, blank=True, help_text=_('Masalan: Years of Equipment Supply Experience'))  # Ko‘rsatkich nomi
    value = models.CharField(_('Qiymat'), max_length=50, null=True, blank=True, help_text=_('Masalan: 10+, 25, 120+'))  # Son/formatlangan matn
    order_index = models.PositiveIntegerField( unique=True, verbose_name=_('Tartib'), help_text=_('Chop etish tartibi'))  # Sortlash

    class Meta:
        verbose_name = _('Statistika bandi')
        verbose_name_plural = _('Statistika bandlari')

    def __str__(self):
        return f"{self.label}: {self.value}"


class FAQ(BaseModel):
    """Tez-tez so‘raladigan savollar: Contact sahifasi ostida ko‘rsatiladi."""
    question = models.CharField(_('Savol'), max_length=255, null=True, blank=True, help_text=_('Ko‘p so‘raladigan savol matni'))  # Savol
    answer = models.TextField(_('Javob'), null=True, blank=True, help_text=_('Savolga javob matni'))  # Javob matni
    order_index = models.PositiveIntegerField(unique=True, verbose_name=_('Tartib'), help_text=_('Chop etish tartibi'))  # Sortlash

    class Meta:
        verbose_name = _('FAQ')
        verbose_name_plural = _('FAQ')

    def __str__(self):
        return self.question


class Inquiry(BaseModel):
    """Kontakt formasi yuborilgan so‘rovlar: adminda ko‘rish, status bilan boshqarish."""
    class INQUIRY_TYPE(models.TextChoices):
        EQUIPMENT = 'equipment', _('Equipment Supply Inquiry')
        TECHNICAL = 'technical', _('Technical Consultation')
        QUOTE = 'quotation', _('Project Quotation Request')
        PARTNERSHIP = 'partnership', _('Partnership Opportunity')
        GENERAL = 'general', _('General Question')

    class PROJECT_SECTOR(models.TextChoices):
        POWER = 'power_generation', _('Power Generation')
        WATER = 'water_wastewater', _('Water & Wastewater')
        OILGAS = 'oil_gas', _('Oil & Gas')
        INDUSTRIAL = 'industrial_manufacturing', _('Industrial Manufacturing')
        RENEWABLE = 'renewable_energy', _('Renewable Energy')
        OTHER = 'other', _('Other')

    class STATUS(models.TextChoices):
        NEW = 'new', _('NEW')
        IN_PROGRESS = 'in_progress', _('In Progress')
        CLOSED = 'closed', _('Closed')

    full_name = models.CharField(_('To‘liq ism'), max_length=160, null=True, blank=True, help_text=_('Murojaatchi to‘liq ismi'))  # F.I.Sh
    company = models.CharField(_('Tashkilot'), max_length=160, null=True, blank=True, help_text=_('Murojaatchi tashkiloti yoki kompaniyasi'))  # Kompaniya nomi
    email = models.EmailField(_('Email'), max_length=254, null=True, blank=True, help_text=_('Aloqa uchun e-pochta manzili'))  # E-mail
    phone = models.CharField(_('Telefon'), max_length=64, null=True, blank=True, help_text=_('Aloqa uchun telefon (ixtiyoriy)'))  # Telefon
    inquiry_type = models.CharField(_('Murojaat turi'), max_length=20, choices=INQUIRY_TYPE.choices, null=True, blank=True, help_text=_('So‘rov turi'))  # Turi
    project_sector = models.CharField(_('Sohasi'), max_length=32, choices=PROJECT_SECTOR.choices, null=True, blank=True, help_text=_('Loyiha sohasi (ixtiyoriy)'))  # Sektor
    message = models.TextField(_('Xabar / tafsilotlar'), null=True, blank=True, help_text=_('Texnik talablar, muddat va boshqa tafsilotlar'))  # Matn
    attachment = models.FileField(upload_to='inquiries/attachments/%Y/%m/', null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'xls', 'xlsx'])], help_text=_('Ilova fayl (PDF, DOC, XLS — 10MB gacha, ixtiyoriy)'))  # Fayl
    consent_updates = models.BooleanField(default=False, verbose_name=_('Yangiliklarga rozilik'), null=True, blank=True, help_text=_('Yangiliklar haqida xabarnoma olishga rozilik'))  # Checkbox
    status = models.CharField(_('Holat'), max_length=20, choices=STATUS.choices, default=STATUS.NEW, help_text=_('Murojaat holati'))  # Workflow status
    ip_address = models.GenericIPAddressField(_('IP manzil'), null=True, blank=True, help_text=_('Murojaat yuborilgan IP manzil (ixtiyoriy)'))  # Audit
    user_agent = models.TextField(_('User-Agent'), null=True, blank=True, help_text=_('Brauzer identifikatori (ixtiyoriy)'))  # Audit

    class Meta:
        verbose_name = _('Murojaat')
        verbose_name_plural = _('Murojaatlar')

    def __str__(self):
        return f"{self.full_name} — {self.get_inquiry_type_display()}"


class DownloadableFile(BaseModel):
    """Yuklab olinadigan fayllar: Brochure, Catalog, Datasheet, Case Study va boshqalar."""
    class FILE_CATEGORY(models.TextChoices):
        BROCHURE = 'brochure', _('Company Brochure')
        CATALOG = 'catalog', _('Equipment Catalog')
        DATASHEET = 'datasheet', _('Technical Datasheet')
        CASE_STUDY = 'case_study', _('Case Study')
        OTHER = 'other', _('Other')

    title = models.CharField(_('Sarlavha'), max_length=200, null=True, blank=True, help_text=_('Fayl sarlavhasi'))  # Nom
    category = models.CharField(_('Kategoriya'), max_length=20, null=True, blank=True, choices=FILE_CATEGORY.choices, help_text=_('Fayl toifasi'))  # Toifa
    description = models.TextField(_('Tavsif'), null=True, blank=True, help_text=_('Qisqa tavsif (ixtiyoriy)'))  # Izoh
    file = models.FileField(upload_to='downloads/%Y/%m/', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx'])], help_text=_('Yuklanadigan fayl'))  # Fayl kontenti
    is_public = models.BooleanField(default=True, verbose_name=_('Ommaviy'), help_text=_('Hamma uchun ko‘rinadimi'))  # Public flag

    class Meta:
        verbose_name = _('Yuklab olinadigan fayl')
        verbose_name_plural = _('Yuklab olinadigan fayllar')

    def __str__(self):
        return self.title


class NewsPost(BaseModel):
    """Yangilik/Blog posti: keyinroq yoqilishi mumkin (status=published bo‘lganda ko‘rinadi)."""
    class STATUS(models.TextChoices):
        DRAFT = 'draft', _('Draft')
        PUBLISHED = 'published', _('Published')

    class CATEGORY(models.TextChoices):
        PROJECT_UPDATES = 'project_updates', _('Project Updates')
        INDUSTRY_NEWS = 'industry_news', _('Industry News')
        COMPANY = 'company_announcements', _('Company Announcements')

    title = models.CharField(_('Sarlavha'), max_length=200, null=True, blank=True, help_text=_('Yangilik sarlavhasi'))  # Sarlavha
    slug = models.SlugField(_('Slug'), max_length=220, unique=True, null=True, blank=True, help_text=_('URL uchun unikal identifikator'))  # URL-friendly
    category = models.CharField(_('Kategoriya'), max_length=40, null=True, blank=True, choices=CATEGORY.choices, help_text=_('Yangilik toifasi'))  # Toifa
    excerpt = models.CharField(_('Qisqa matn'), max_length=255, null=True, blank=True, help_text=_('Qisqa kirish matni (ixtiyoriy)'))  # Qisqa preview
    body = models.TextField(_('Matn'), null=True, blank=True, help_text=_('To‘liq matn'))  # Kontent
    cover_image = models.ImageField(upload_to='news/covers/%Y/%m/', null=True, blank=True, help_text=_('Muqova rasmi (ixtiyoriy)'))  # Muqova
    status = models.CharField(_('Holat'), max_length=12, choices=STATUS.choices, default=STATUS.DRAFT, help_text=_('Nashr holati'))  # Draft/Published
    published_at = models.DateTimeField(_('E’lon vaqti'), null=True, blank=True, help_text=_('Nashr qilingan sana-vaqt (ixtiyoriy)'))  # Publish time

    class Meta:
        verbose_name = _('Yangilik')
        verbose_name_plural = _('Yangiliklar')

    def __str__(self):
        return self.title


class Testimonial(BaseModel):
    """Mijoz/hamkor fikrlari: homepage slider yoki alohida sahifa uchun."""
    author_name = models.CharField(_('Muallif'), max_length=160, help_text=_('Fikr muallifi to‘liq ismi'))  # Muallif
    author_role = models.CharField(_('Lavozim/roli'), max_length=160, null=True, blank=True, help_text=_('Muallif lavozimi (ixtiyoriy)'))  # Role/Title
    company = models.CharField(_('Tashkilot'), max_length=160, null=True, blank=True, help_text=_('Muallif tashkiloti (ixtiyoriy)'))  # Kompaniya
    quote = models.TextField(_('Fikr-mulohaza'), help_text=_('Testimonial matni'))  # Iqtibos
    photo = models.ImageField(upload_to='testimonials/%Y/%m/', null=True, blank=True, help_text=_('Muallif surati (ixtiyoriy)'))  # Avatar
    is_featured = models.BooleanField(default=True, verbose_name=_('Tavsiya etilgan'), help_text=_('Bosh sahifada ajratib ko‘rsatish'))  # Flag

    class Meta:
        verbose_name = _('Testimonial')
        verbose_name_plural = _('Testimonials')

    def __str__(self):
        return f"{self.author_name} — {self.company or ''}".strip()

class Banner(BaseModel):
    """Banner: homepage slider sahifa uchun."""
    order_index = models.PositiveIntegerField(unique=True, verbose_name=_('Tartib'), null=True,
                                              help_text=_('Chop etish tartibi'))  # Sortlash
    title = models.CharField(_('Muallif'), max_length=160, help_text=_('Fikr muallifi to‘liq ismi'))  # Muallif
    description = models.TextField(_('Izoh'), help_text=_('Testimonial matni'))  # Iqtibos
    photo = models.ImageField(upload_to='banner/%Y/%m/', null=True, blank=True, help_text=_('Muallif surati (ixtiyoriy)'))  # Avatar
    is_featured = models.BooleanField(default=True, verbose_name=_('Tavsiya etilgan'), help_text=_('Bosh sahifada ajratib ko‘rsatish'))  # Flag

    class Meta:
        verbose_name = _('Banner')
        verbose_name_plural = _('Banneres')

    def __str__(self):
        return f"{self.title}".strip()


class OurWork(BaseModel):
    """Bizning ishlarimiz..."""
    class TYPE(models.TextChoices):
        TYPE1 = 'why_choose ', _('Why Choose Optivora')
        TYPE2 = 'technical_solution ', _('Technical Solution')
        TYPE3 = 'what_we_do', _('What We Do')
        TYPE4 = 'our_suppliers', _('Our Suppliers')
        TYPE5 = 'industries_we_serve', _('Industries We Serve')

    title = models.CharField(_('Xizmat nomi'), null=True, blank=True, max_length=150, unique=True, help_text=_('Xizmatning to‘liq nomi (masalan: Equipment Supply & Procurement)'))  # Unikal nom
    description = models.TextField(_('Batafsil tavsif'), null=True, blank=True, help_text=_('Xizmat tafsilotlari (ixtiyoriy)'))  # Batafsil matn
    icon = models.ImageField(upload_to='ourwork/icons/%Y/%m/', null=True, blank=True, help_text=_('Xizmat ikonkasi (ixtiyoriy)'))  # UI ikona
    type = models.CharField(_('Holat'), max_length=50, choices=TYPE.choices, null=True, blank=True, help_text=_('Nashr holati'))
    order_index = models.PositiveIntegerField( verbose_name=_('Tartib'), help_text=_('Chop etish tartibi'))  # Sortlash

    class Meta:
        verbose_name = _('Our Work')
        verbose_name_plural = _('Our Works')

    def __str__(self):
        return self.title