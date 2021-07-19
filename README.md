# cheat-sheets


# Misc

Quick script to convert multiple .cbr files to 1 pdf
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

Another quick script to rename multiple folders of .cbr files ( very poorly done )
```bash
for d in */ ; do
    echo "$d"
    ls "$d"
    rm "$d"*.jpg
    rm "$d"*.rar
    rm *.jpg
    rm *.rar
    for f in "$d"*.cbr; do 
        cp -- "$f" "${f%.cbr}.rar"
    done
    for f in "$d"*.rar; do 
        unrar e "$f"
        echo $f
    done
    img2pdf *.jpg --output "$d"Naruto:\ Volume.pdf
    rm "$d"*.jpg
    rm "$d"*.rar
    rm *.jpg
    rm *.rar
done
```
