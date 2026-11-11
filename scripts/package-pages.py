from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
root=Path.cwd()
out=root/'output'
out.mkdir(exist_ok=True)
entries=['.github','.gitignore','src','public','e2e','scripts','package.json','package-lock.json','index.html','vite.config.ts','tsconfig.json','playwright.config.ts','README.md']
with ZipFile(out/'github-pages-project.zip','w',ZIP_DEFLATED) as archive:
 for entry in entries:
  target=root/entry
  for file in sorted(target.rglob('*')) if target.is_dir() else [target]:
   if file.is_file(): archive.write(file,file.relative_to(root).as_posix())
with ZipFile(out/'github-pages-static.zip','w',ZIP_DEFLATED) as archive:
 for file in sorted((root/'dist').rglob('*')):
  if file.is_file(): archive.write(file,file.relative_to(root/'dist').as_posix())
for name in ['github-pages-project.zip','github-pages-static.zip']:
 with ZipFile(out/name) as archive:
  assert archive.testzip() is None
  print(name, (out/name).stat().st_size, 'bytes,',len(archive.namelist()),'files')
