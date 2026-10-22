import unittest

from enhancer import detect_type, enhance, extract_numbers


class TestDetectType(unittest.TestCase):
    def test_content_persian(self):
        self.assertEqual(detect_type("یه ریل اینستاگرام با کپشن خوب بساز"), "content")

    def test_code(self):
        self.assertEqual(detect_type("تو گیت‌هاب یه اسکریپت پایتون بنویس"), "code")

    def test_sales(self):
        self.assertEqual(detect_type("یه آگهی دیوار برای فروش بیشتر بنویس"), "sales")

    def test_general_fallback(self):
        self.assertEqual(detect_type("سلام خوبی"), "general")


class TestEnhance(unittest.TestCase):
    def test_sections_present(self):
        out = enhance("یه ریل اینستاگرام بساز")
        for section in ("## Goal", "## Context", "## Deliverables",
                        "## Constraints", "## Success criteria"):
            self.assertIn(section, out)

    def test_numbers_preserved_verbatim(self):
        out = enhance("کارت گرافیک ۲.۳ میلیاردی، بودجه 4500000 تومان، پیج 12.5k فالوور")
        self.assertIn("۲.۳", out)
        self.assertIn("4500000", out)
        self.assertIn("12.5", out)

    def test_phone_and_name_preserved(self):
        out = enhance("مغازه خدمات کامپیوتری سینا، تلفن 09185790374، ساعت ۸ تا ۹")
        self.assertIn("09185790374", out)
        self.assertIn("خدمات کامپیوتری سینا", out)

    def test_quoted_name_listed(self):
        out = enhance("برای «خدمات کامپیوتری سینا» آگهی بنویس")
        self.assertIn("خدمات کامپیوتری سینا", out.split("preserve")[-1])

    def test_checklist_by_type(self):
        self.assertIn("Hook", enhance("ریل اینستاگرام بساز"))

    def test_extract_numbers(self):
        nums = extract_numbers("قیمت ۱۲٬۵۰۰ و 3 تا")
        self.assertIn("۱۲٬۵۰۰", nums)


if __name__ == "__main__":
    unittest.main()
