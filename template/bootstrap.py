import shutil, sys, datetime
from pathlib import Path

def main():
    tools = False
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if "--tools" in sys.argv:
        tools = True

    if len(args) < 1:
        print("Usage: python bootstrap.py <project-dir> [--tools]")
        print("  --tools  Also copy template/resources/ into project .agent/")
        sys.exit(1)

    dst = Path(args[0]).resolve()
    project_name = dst.name
    today = datetime.date.today().isoformat()

    # Copy .agent skeleton
    base = Path(__file__).parent
    if (dst / ".agent").exists():
        print(f".agent/ already exists at {dst}")
    else:
        shutil.copytree(base / ".agent", dst / ".agent")
        print(f"Copied .agent/ to {dst}")

    # Replace placeholders
    for f in (dst / ".agent").rglob("*"):
        if f.is_file():
            text = f.read_text(encoding="utf-8")
            text = text.replace("{{project_name}}", project_name)
            text = text.replace("{{date}}", today)
            f.write_text(text, encoding="utf-8")
            print(f"  Processed: {f.relative_to(dst / '.agent')}")

    # Copy template resources/ if requested
    if tools:
        src = base / "resources"
        if src.exists():
            dst_res = dst / ".agent" / "Resources"
            shutil.copytree(src, dst_res)
            print(f"Copied template resources/ to .agent/Resources/")

    # .gitignore
    gitignore = dst / ".gitignore"
    if gitignore.exists():
        lines = gitignore.read_text(encoding="utf-8").splitlines()
        if ".agent/" not in lines:
            gitignore.write_text(
                gitignore.read_text(encoding="utf-8").strip() + "\n.agent/\n",
                encoding="utf-8"
            )
            print(f"Appended .agent/ to existing .gitignore")
    else:
        gitignore.write_text(".agent/\n", encoding="utf-8")
        print("Created .gitignore with .agent/")

    print(f"\nDone. Run: mneme.switch_scope('{project_name}')")

if __name__ == "__main__":
    main()
