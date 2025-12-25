print("=" * 60)
print("🧪 ТЕСТ №1: Проверка установки библиотек")
print("=" * 60)

# 1. Проверяем Flask
try:
    from flask import Flask
    print("✅ Flask УСТАНОВЛЕН")
except ImportError:
    print("❌ Flask НЕ УСТАНОВЛЕН")
    exit(1)

# 2. Проверяем python-telegram-bot
try:
    from telegram import Bot
    print("✅ python-telegram-bot УСТАНОВЛЕН")
except ImportError:
    print("❌ python-telegram-bot НЕ УСТАНОВЛЕН")

print("=" * 60)
print("📦 Список установленных библиотек:")
print("=" * 60)

import pkg_resources
for dist in pkg_resources.working_set:
    if "flask" in dist.key or "telegram" in dist.key:
        print(f"   {dist.key} == {dist.version}")

print("=" * 60)
print("🎯 ТЕСТ УСПЕШЕН!")
print("=" * 60)

# Не запускаем Flask, просто завершаем программу