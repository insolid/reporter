import argparse
from .services import PerformanceReport, SkillQtyReport

REPORTS = {"performance", "skill"}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--files", nargs="*", required=True)
    parser.add_argument("--report", required=True, choices=REPORTS)

    args, _ = parser.parse_known_args()
    files = args.files
    report = args.report

    if report == "performance":
        parser.parse_args()
        res = PerformanceReport().generate(files, as_table=True)

    # Пример добавления другого отчета
    elif report == "skill":
        parser.add_argument("--skill_name", required=True)
        skill_name = parser.parse_args().skill_name
        res = SkillQtyReport().generate(files, skill_name)

    print(res)


if __name__ == "__main__":
    main()
