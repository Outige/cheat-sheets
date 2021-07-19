# cheat-sheets


# Misc

## Quick script to convert multiple .cbr files to 1 pdf
```bash
# copy all cbr to rar
for f in *.cbr; do 
    cp -- "$f" "${f%.cbr}.rar"
done

for f in *.rar; do 
    unrar e $f
done

img2pdf *.jpg --output combined.pdf

rm *.jpg
rm *.rar
```
