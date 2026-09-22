# دليل ربط المشروع بقاعدة بيانات PostgreSQL والـ CRUD و الـ Admin Dashboard

هذا المشروع يحتوي على تطبيق Django متكامل مربوط بقاعدة بيانات **PostgreSQL** مع تطبيق كامل لعمليات **CRUD** (قراءة، إضافة، تعديل، حذف) في التطبيقات الثلاثة، وتشغيل وتخصيص لوحة تحكم الأدمن **Django Admin Dashboard**.

---

## 🗄️ إعدادات قاعدة البيانات (PostgreSQL Settings)

تم ضبط إعدادات الـ PostgreSQL في ملف [`myproject/settings.py`](file:///c:/Users/mazen/Downloads/myproject(1)/myproject/myproject/settings.py):

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'myproject_db',      # اسم قاعدة البيانات
        'USER': 'postgres',          # اسم المستخدم
        'PASSWORD': 'postgres',      # كلمة المرور
        'HOST': 'localhost',         # السيرفر المحلي
        'PORT': '5432',              # البورت الافتراضي لـ PostgreSQL
    }
}
```

---

## 📦 تفاصيل عمليات الـ CRUD في التطبيقات الثلاثة

### 1. App 1: المقالات (Articles)
- **النموذج (Model)**: [`app1/models.py`](file:///c:/Users/mazen/Downloads/myproject(1)/myproject/app1/models.py) (`Article`)
- **Insert (إضافة)**: نموذج إدخال في الصفحة الرئيسية وحفظ عبر `create_article`.
- **Read (قراءة)**: عرض كل المقالات من قاعدة البيانات عبر `Article.objects.all()`.
- **Update (تعديل)**: زر "تعديل ✏️" ينقلك لصفحة تعديل مقال مخصص وحفظ التغييرات عبر `edit_article`.
- **Delete (حذف)**: زر "حذف 🗑️" لحذف المقال من قاعدة البيانات عبر `delete_article`.
- **Admin Dashboard**: مسجل مع بحث في العنوان والمحتوى وفلاتر للتاريخ.

---

### 2. App 2: المهام (Tasks / To-Do)
- **النموذج (Model)**: [`app2/models.py`](file:///c:/Users/mazen/Downloads/myproject(1)/myproject/app2/models.py) (`Task`)
- **Insert (إضافة)**: نموذج إضافة مهمة جديدة مباشرة عبر `create_task`.
- **Read (قراءة)**: عرض كل المهام مع تمييز المكتملة وغير المكتملة.
- **Update (تعديل)**: 
  - تعديل تفاصيل المهمة كاملة من صفحة `edit_task`.
  - تبديل سريع لحالة الإنجاز (Done/Undone) بزر تفاعلي مباشر عبر `toggle_task`.
- **Delete (حذف)**: زر "حذف 🗑️" لحذف المهمة عبر `delete_task`.
- **Admin Dashboard**: مسجل مع ميزة **`list_editable`** لتعديل حالة الإنجاز مباشرة من جدول الأدمن دون فتح السجل!

---

### 3. App 3: جهات الاتصال (Contacts)
- **النموذج (Model)**: [`app3/models.py`](file:///c:/Users/mazen/Downloads/myproject(1)/myproject/app3/models.py) (`Contact`)
- **Insert (إضافة)**: تسجيل جهة اتصال جديدة (الاسم، الإيميل، الهاتف، ملاحظات) عبر `create_contact`.
- **Read (قراءة)**: عرض دليل جهات الاتصال مع عدد السجلات المسجلة.
- **Update (تعديل)**: زر "تعديل ✏️" لتعديل بيانات جهة الاتصال وحفظها عبر `edit_contact`.
- **Delete (حذف)**: زر "حذف 🗑️" لحذف جهة الاتصال عبر `delete_contact`.
- **Admin Dashboard**: مسجل مع إمكانية البحث بالاسم والإيميل والهاتف والفرز حسب التاريخ.

---

## 🛡️ لوحة تحكم الأدمن (Admin Dashboard)

تم تفعيل وتخصيص لوحة تحكم الأدمن بالكامل:
- **العنوان والشعار**: "لوحة تحكم إدارة النظام | Admin Dashboard"
- **الموديلات المسجلة**: Articles, Tasks, Contacts
- **الرابط**: `http://127.0.0.1:8000/admin/`

---

## 🚀 خطوات التشغيل (عند الرغبة في عمل Run):

1. **تأكد من إنشاء قاعدة البيانات في PostgreSQL**:
   ```sql
   CREATE DATABASE myproject_db;
   ```

2. **تثبيت المكتبات**:
   ```bash
   pip install -r requirements.txt
   ```

3. **تطبيق الـ Migrations الجاهزة**:
   ```bash
   python manage.py migrate
   ```

4. **إنشاء حساب الأدمن تلقائياً بأمر واحد**:
   ```bash
   python manage.py setup_admin
   ```
   *أو عبر الأمر التقليدي:*
   ```bash
   python manage.py createsuperuser
   ```

5. **تشغيل السيرفر**:
   ```bash
   python manage.py runserver
   ```

ثم تصفح الروابط:
- المقالات: `http://127.0.0.1:8000/app1/`
- المهام: `http://127.0.0.1:8000/app2/`
- جهات الاتصال: `http://127.0.0.1:8000/app3/`
- لوحة الأدمن: `http://127.0.0.1:8000/admin/`
