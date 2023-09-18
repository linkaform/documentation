
echo 'Building LinkaForm Documentation'
cd /srv/docs/
sphinx-build -c /srv/docs/ content/ build/
echo 'Building done..'
