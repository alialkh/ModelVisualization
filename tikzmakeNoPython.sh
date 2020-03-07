pdflatex $1.tex

rm *.aux *.log *.vscodeLog
cp *.tex pastRuns/pastRun.tex
rm *.tex

if [[ "$OSTYPE" == "darwin"* ]]; then
    open $1.pdf
else
    xdg-open $1.pdf
fi

