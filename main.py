#!/usr/bin/env python3
"""CLI: turn a raw task message into a professional structured prompt.

Usage:
  python3 main.py "یه ریل اینستا بساز راجب کارت گرافیک ۲.۳ میلیاردی"
  python3 main.py --demo
  python3 main.py --type code "یه اسکریپت بساز"
"""
import argparse
import sys

from enhancer import enhance

DEMOS = [
    "یه ریل اینستاگرام بساز راجب کارت گرافیک RTX 5090 که ۲.۳ میلیارد تومان قیمتشه، پیج sarzamin_game11",
    "تو گیت‌هاب یه ایجنت پایتون بساز که قیمت قطعات رو چک کنه، بودجه پروژه ۵ میلیون تومان",
    "برای مغازه «خدمات کامپیوتری سینا» تو اراک یه آگهی دیوار بنویس، نصب ویندوز ۴۵۰ هزار تومان، تلفن 09185790374",
]


def main():
    ap = argparse.ArgumentParser(description="Persian prompt enhancer")
    ap.add_argument("text", nargs="?", help="raw task message")
    ap.add_argument("--demo", action="store_true", help="run 3 built-in samples")
    ap.add_argument("--type", dest="task_type", default=None,
                    help="force a type: content|code|shop|sales|research|general")
    args = ap.parse_args()
    if args.demo:
        for i, sample in enumerate(DEMOS, 1):
            print(f"\n{'=' * 20} DEMO {i} {'=' * 20}\n")
            print(enhance(sample))
        return 0
    if not args.text:
        ap.print_help()
        return 2
    print(enhance(args.text, args.task_type))
    return 0


if __name__ == "__main__":
    sys.exit(main())
