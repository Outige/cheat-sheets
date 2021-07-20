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
    cd "$d"

    #copy all cbr to rar
    for f in *.cbr; do 
        cp -- "$f" "${f%.cbr}.rar"
    done

    for f in *.rar; do 
        unrar e "$f"
        # FIXME: some of the cbr files have clasing names. The best way to get around this....
        # $ make a pdf of the currently extracted rar
        # $ rm *.jpg
    done
    # $ merge all pdfs

    img2pdf *.jpg --output Naruto:\ Volume.pdf

    rm *.jpg
    rm *.rar

    cd ..
done
```
