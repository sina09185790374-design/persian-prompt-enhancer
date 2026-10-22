# Persian Prompt Enhancer ✨

Turn a raw, messy task message (Persian or English) into a **professional structured prompt** — Goal / Context / Deliverables / Constraints / Success criteria — with type-specific checklists.

Born in a real workflow: every task for our AI shop-automation system passes through this enhancer before execution. Stdlib-only Python, no API keys, no network.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB) ![License](https://img.shields.io/badge/license-MIT-green) ![Deps](https://img.shields.io/badge/deps-stdlib%20only-brightgreen)

## What it does
- **Detects the task type** from keywords: `content` · `code` · `shop` · `sales` · `research` · `general`
- **Extracts the goal** (first real sentence) and fills the full template
- **Preserves your exact values verbatim** — numbers, prices (۲.۳ میلیارد، 4500000 تومان), phone numbers and «quoted names» are carried into the output unchanged and listed explicitly
- **Adds a deliverable checklist per type** (e.g. content → hook in 1–3s, 9:16 video, CTA; code → tests pass, no secrets, README)

## Quick start
```bash
python3 main.py "یه ریل اینستاگرام بساز راجب کارت گرافیک ۲.۳ میلیاردی، پیج sarzamin_game11"
python3 main.py --demo          # 3 built-in samples
python3 main.py --type code "یه اسکریپت بساز که قیمت‌ها رو چک کنه"
```

Sample output (abridged):
```markdown
# Professional Prompt
**Task type:** Content production (`content`)
## Goal
یه ریل اینستاگرام بساز راجب کارت گرافیک ۲.۳ میلیاردی، پیج sarzamin_game11
## Deliverables
- [ ] Hook in the first 1–3 seconds
- [ ] Video-first format (9:16 for reels)
...
**Exact values to preserve:** ۲.۳ · sarzamin_game11
```

## Tests
```bash
python3 -m unittest discover -s tests -v   # 10 tests
```

## فارسی 🇮🇷
پیام خام و شلخته‌ت رو می‌گیره و تبدیلش می‌کنه به یه پرامپت حرفه‌ای و ساخت‌یافته: هدف، کانتکست، خروجی‌های دقیق، محدودیت‌ها و معیار موفقیت. نوع تسک رو خودش تشخیص می‌ده (محتوا، کد، مغازه، فروش، تحقیق) و چک‌لیست مخصوص همون نوع رو اضافه می‌کنه. مهم‌تر از همه: عددها، قیمت‌ها و اسم‌هایی که نوشتی **دقیقا بدون تغییر** می‌رن تو خروجی — هیچ عددی ساخته یا گم نمی‌شه. فقط با کتابخانه استاندارد پایتون، بدون هیچ وابستگی.

ساخته‌شده در «خدمات کامپیوتری سینا» — اراک. سفارش ایجنت اختصاصی: تلگرام [@sarzamin_game11](https://t.me/sarzamin_game11)

## License
MIT
