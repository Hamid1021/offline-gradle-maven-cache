
# Offline Gradle + Maven Cache  
## ساخته شده توسط Mr.Hidden | Created by Mr.Hidden

💡 This repository is designed to help developers — especially in countries facing connectivity issues or sanctions — build Android or React Native projects **offline** using a pre-cached Gradle and Maven repository.

---

## 🇮🇷 راهنمای فارسی

### 📦 فایل‌های قابل دانلود
| نام فایل | کاربرد |
|----------|--------|
| [`full-gradle-cache.tar.gz`](https://github.com/Hamid1021/offline-gradle-maven-cache/releases/download/gradle-maven/full-gradle-cache.tar.gz) | کش کامل Gradle برای مسیر `~/.gradle` یا `%USERPROFILE%\.gradle` |
| [`gradle-maven.tar.gz`](https://github.com/Hamid1021/offline-gradle-maven-cache/releases/download/gradle-maven/gradle-maven.tar.gz) | کش ساختار یافته‌ی Maven، قابل استفاده به عنوان لوکال ریپازیتوری یا سرور mirror |

---

### 🖥 نحوه استفاده در لینوکس و ویندوز

#### 1. کش Gradle (برای بیلد آفلاین)
**لینوکس:**
```bash
tar -xzvf full-gradle-cache.tar.gz -C ~/.gradle
````

**ویندوز (PowerShell):**

```powershell
tar -xvzf full-gradle-cache.tar.gz -C $env:USERPROFILE\.gradle
```

---

#### 2. استفاده از کش Maven

**اکسترکت فایل:**

**Linux:**

```bash
mkdir -p ~/offline-maven-repo
tar -xzvf gradle-maven.tar.gz -C ~/offline-maven-repo
```

**Windows (PowerShell):**

```powershell
mkdir "$env:USERPROFILE\offline-maven-repo"
tar -xvzf gradle-maven.tar.gz -C "$env:USERPROFILE\offline-maven-repo"
```

سپس در فایل `settings.gradle` یا `build.gradle` این خط را اضافه کنید:

```groovy
maven {
    url uri(System.getenv("USERPROFILE") + "/offline-maven-repo") // ویندوز
}
```

یا:

```groovy
maven {
    url uri("${System.properties['user.home']}/offline-maven-repo") // لینوکس/مک
}
```

---

### 🌐 استفاده به‌صورت سرور آنلاین (mirror)

این ریپو به‌گونه‌ای ساختاربندی شده که بتوانید از آن مانند یک remote Maven repository استفاده کنید:

```groovy
maven {
    url "https://hamid1021.github.io/offline-gradle-maven-cache"
}
```

> ⚠️ توجه: از آن‌جایی که GitHub Pages فایل‌های `.pom`, `.aar`, `.jar` را مستقیماً در دسترس قرار می‌دهد، Gradle می‌تواند از آن‌ها استفاده کند، ولی بهتر است به صورت لوکال اکسترکت شده استفاده شود تا از مشکل سرعت و محدودیت‌های CDN جلوگیری شود.

---

## 🇺🇸 English Guide

### 📦 Downloadable Files

| File Name                                                                                                                                     | Description                                                                                |
| --------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| [`full-gradle-cache.tar.gz`](https://github.com/Hamid1021/offline-gradle-maven-cache/releases/download/gradle-maven/full-gradle-cache.tar.gz) | Full Gradle cache to place inside `~/.gradle` (Linux) or `%USERPROFILE%\.gradle` (Windows) |
| [`gradle-maven.tar.gz`](https://github.com/Hamid1021/offline-gradle-maven-cache/releases/download/gradle-maven/gradle-maven.tar.gz)           | Offline Maven-style directory that can be used as a local repo or hosted as a mirror       |

---

### 🖥 Usage on Linux and Windows

#### 1. Gradle Cache (Offline Builds)

**Linux:**

```bash
tar -xzvf full-gradle-cache.tar.gz -C ~/.gradle
```

**Windows (PowerShell):**

```powershell
tar -xvzf full-gradle-cache.tar.gz -C $env:USERPROFILE\.gradle
```

---

#### 2. Use as Local Maven Repository

**Extract the files**:

**Linux:**

```bash
mkdir -p ~/offline-maven-repo
tar -xzvf gradle-maven.tar.gz -C ~/offline-maven-repo
```

**Windows (PowerShell):**

```powershell
mkdir "$env:USERPROFILE\offline-maven-repo"
tar -xvzf gradle-maven.tar.gz -C "$env:USERPROFILE\offline-maven-repo"
```

Then in your `settings.gradle` or `build.gradle`:

```groovy
maven {
    url uri(System.getenv("USERPROFILE") + "/offline-maven-repo") // Windows
}
```

Or:

```groovy
maven {
    url uri("${System.properties['user.home']}/offline-maven-repo") // Linux/macOS
}
```

---

### 🌍 Use as Remote Maven Mirror

You can also use GitHub Pages version as a remote Maven mirror:

```groovy
maven {
    url "https://hamid1021.github.io/offline-gradle-maven-cache"
}
```

> ⚠️ Note: While this works in many cases, for large builds or production-grade apps, local usage is preferred due to CDN and rate limits.

---

🔧 Maintained by **Mr.Hidden**
🌐 [GitHub Repo](https://github.com/Hamid1021/offline-gradle-maven-cache)
🌍 [Live GitHub Pages Mirror](https://hamid1021.github.io/offline-gradle-maven-cache/)
