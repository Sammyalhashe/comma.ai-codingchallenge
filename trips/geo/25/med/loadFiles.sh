for f in *.json
do
echo "Processing $f file...";
mkdir processed;
mongoimport --file $f -d comma -c trips_med && mv $f processed/$f;
done

# -u $1 -p $2 --authenticationDatabase admin
