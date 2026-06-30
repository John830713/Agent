import shutil, sys, re, datetime
from pathlib import Path

def main():
    if len(sys.argv) < 2:
        print("Usage: python bootstrap.py <project-dir>")
        sys.exit(1)

    dst = Path(sys.argv[1]).resolve()
    src = Path(__file__).parent / ".agent"
    project_name = dst.name
    today = datetime.date.today().isoformat()

    # Copy .agent skeleton
    if (dst / ".agent").exists():
        print(f".agent/ already exists at {dst}")
    else:
        shutil.copytree(src, dst / ".agent")
        print(f"Copied .agent/ to {dst}")

    # Replace placeholders
    for f in (dst / ".agent").rglob("*"):
        if f.is_file():
            text = f.read_text(encoding="utf-8")
            text = text.replace("{{project_name}}", project_name)
            text = text.replace("{{date}}", today)
            f.write_text(text, encoding="utf-8")
            print(f"  Processed: {f.relative_to(dst / '.agent')}")

    # .gitignore
    gitignore = dst / ".gitignore"
    if gitignore.exists():
        lines = gitignore.read_text(encoding="utf-8").splitlines()
        if ".agent/" not in lines:
            gitignore.write_text(
                gitignore.read_text(encoding="utf-8").rstrip() + "\n.agent/\n",
                encoding="utf-8"
            )
            print("Appended .agent/ to existing .gitignore")
    else:
        gitignore.write_text(".agent/\n", encoding="utf-8")
        print("Created .gitignore with .agent/")

    print(f"\nDone. Run: mneme.switch_scope('{project_name}')")

if __name__ == "__main__":
    main()
