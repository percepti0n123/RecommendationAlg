# markdown_report.py
import pandas as pd

def save_markdown_report(df: pd.DataFrame, path: str, student_id: int):
    """
    Сохраняет рекомендации в виде markdown-отчета с пояснением
    """
    with open(path, 'w', encoding='utf-8') as f:
        f.write(f"# 📘 Отчет по рекомендациям для студента {student_id}\n\n")
        f.write("## 📌 Обоснование\n")
        f.write("Система рекомендует задания на основе сочетания:\n")
        f.write("- индивидуальных предпочтений ученика (анкета)\n")
        f.write("- прогресса по темам (если прогресс < 70%)\n")
        f.write("- анализа заданий, решённых похожими учениками (коллаборативный фильтр)\n\n")

        f.write("## 📊 Список рекомендаций\n\n")
        f.write("| ID задания | Тема | Причина рекомендации | Источник |\n")
        f.write("|------------|------|-----------------------|----------|\n")

        for _, row in df.iterrows():
            task_id = row.get("id", "")
            theme = row.get("theme_name", "")
            reason = row.get("explanation", "")
            source = row.get("source", "")
            f.write(f"| {task_id} | {theme} | {reason} | {source} |\n")

        f.write("\n_Сгенерировано автоматически системой рекомендаций._")

        print(f"📄 Markdown-отчет сохранен в {path}")

def save_readiness_report(df: pd.DataFrame, path: str, student_id: int):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(f"# 🧠 Анализ готовности по темам для студента {student_id}\n\n")
        f.write("Оценка прогресса и рекомендации по действиям:\n\n")
        f.write("| Тема | Прогресс (%) | Состояние | Рекомендация |\n")
        f.write("|------|----------------|------------|-----------------------------|\n")
        for _, row in df.iterrows():
            theme = row.get("theme_name", "")
            progress = row.get("progress", 0)
            state = row.get("состояние", "")
            action = row.get("рекомендация", "")
            f.write(f"| {theme} | {progress:.1f} | {state} | {action} |\n")

        # Итоговый вывод
        f.write("\n## 📌 Итоговая рекомендация\n")
        weak_themes = df[df["состояние"] == "не готов"]["theme_name"].tolist()
        if weak_themes:
            f.write("Ученику стоит сосредоточиться на следующих темах: \n")
            for t in weak_themes:
                f.write(f"- {t}\n")
        else:
            f.write("Поздравляем! У студента нет тем, по которым он полностью не готов. 🎉\n")

        f.write("\n_Сформировано на основе данных из таблицы StudentThemeProgress._")

        print(f"📄 Markdown-отчет готовности сохранен в {path}")