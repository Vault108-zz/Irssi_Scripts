echo "starting"

echo "making directory"

mkdir 	~/.irssi/scripts

echo "directory made"

mv *.py ~/.irssi/scripts

echo "done Moving"

cd  ..

rm -fr ~/.irssi/scripts/install.py

rm -fr Irssi_Scripts/

echo "done"

