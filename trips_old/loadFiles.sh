for f in *.json
do
echo "Processing $f file...";
mongoimport --file $f -d comma -c trips && mv $f $f.processed;
done

# -u $1 -p $2 --authenticationDatabase admin
