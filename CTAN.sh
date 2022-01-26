#last run: 
#Program to download all CTAN Latex documentation and store it locally
set -x
cat <(echo "#last run:" $(date +'%c')) <(tail -n +2 "$0") > .temp
cd "$(dirname "$0")"
[ -d "Source" ] || mkdir Source
[ -d "Docs" ] || mkdir Docs
curl "https://ctan.math.washington.edu/tex-archive/macros/latex/contrib/" |
tee index.html |
grep "<a href=\".*\.zip" |
cut -b 85- | cut -d \. -f 1 |
{
	while read package; do
		[ -d "Source/$package" ] || mkdir Source/$package
		[ -d "Docs/$package" ] || mkdir Docs/$package
		curl "https://ctan.math.washington.edu/tex-archive/macros/latex/contrib/$package.zip" > $package.zip
		unzip $package.zip -d Source/$package
		rm $package.zip
		ln -s $(find Source/$package -name $package.pdf) Docs/$package.pdf
	done
}
rm *.pdf
mv .temp "$0"
