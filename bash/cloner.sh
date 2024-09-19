## Create a loop of repo names here
declare -a arr=(
	"a-repo-name-1"
	"a-repo-name-2"
)

## Then iterate through the loop and run these commands:
for i in "${arr[@]}"
do
	git clone git@github.com:marketjs-client-projects/"$i".git
	
	cd "$i"
	
	cd ..
done
