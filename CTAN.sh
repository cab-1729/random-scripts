#last run: 
#Program to download all CTAN Latex documentation and store it locally
set -x #show commands
cat <(echo "#last run:" $(date +'%c')) <(tail -n +2 "$0") > .temp #store file with new date
cd "$(dirname "$0")" #be proper directory
[ -d "Source" ] || mkdir Source;[ -d "Docs" ] || mkdir Docs;[ -d "Pages" ] || mkdir Pages #make directories
rm Docs/*;rm -r Source/* #clean existing documentation
function server(){ #get all documentation hosted at server
	mkdir "Source/$2"
	curl $1 |
	tee "Pages/$2.html" |
	grep "<a href=\".*\.zip" |
	cut -b $3- | cut -d \. -f 1 |
	{
		while read package; do
			curl "$1$package.zip" > $package.zip
			unzip $package.zip -d "Source/$2"
			rm $package.zip
			doc=$(find "Source/$2/$package" -name $package.pdf | tail -n 1)
			[ -z "$doc" ] || ln -s "$(pwd)/$doc" Docs/$package.pdf
		done
	}
}
#get CTAN
server "https://ctan.math.washington.edu/tex-archive/macros/latex/contrib/" "latex" 85
server "https://ctan.math.illinois.edu/macros/luatex/latex/" "luatex" 10
server "https://mirrors.mit.edu/CTAN/macros/unicodetex/latex/" "unicodetex" 10
# replace file with proper date
mv .temp "$0"
