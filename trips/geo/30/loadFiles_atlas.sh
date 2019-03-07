for f in *.json
do
echo "Processing $f file...";
mkdir processed;
#mongoimport --file $f -d comma -c trips_small && mv $f processed/$f;
mongoimport --host dashcamroutes-shard-00-00-i9nb6.mongodb.net:27017 --file $f --type json -d comma -c trips_med --authenticationDatabase admin --ssl -u alhashe2 -p Rfin1ihe && mv $f processed/$f;
done

# -u $1 -p $2 --authenticationDatabase admin
