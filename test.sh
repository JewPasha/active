echo "Testing --help"
read -p "Press any key to continue... " -n1 -s
echo ""
python3 tinyscanner.py --help
echo ""
echo "Testing invalid command"
read -p "Press any key to continue... " -n1 -s
echo ""
python3 tinyscanner.py 1.1.1.1 -p 80
echo ""
echo "Testing out of range port"
read -p "Press any key to continue... " -n1 -s
echo ""
python3 tinyscanner.py -u 1.1.1.1 -p 80-70000
echo ""
echo "Testing invalid port"
read -p "Press any key to continue... " -n1 -s
echo ""
python3 tinyscanner.py -t 1.1.1.1 -p port-ports
echo ""
echo "Testing various scan types on google's dns server 8.8.8.8"
read -p "Press any key to continue... " -n1 -s
echo ""
echo "TCP port 53 should be open"
python3 tinyscanner.py -t 8.8.8.8 -p 53
echo ""
echo "TCP port 54 should be closed"
python3 tinyscanner.py -t 8.8.8.8 -p 54
echo ""
echo "UDP port 53 should be open"
python3 tinyscanner.py -u 8.8.8.8 -p 53
echo ""
echo "UDP port 54 should be closed"
python3 tinyscanner.py -u 8.8.8.8 -p 54
echo ""
echo "Testing port ranges on google's dns server 8.8.8.8"
read -p "Press any key to continue... " -n1 -s
echo ""
echo "only TCP port 53 should be open"
python3 tinyscanner.py -t 8.8.8.8 -p 52-54
echo ""
echo "only UDP port 53 should be open"
python3 tinyscanner.py -u 8.8.8.8 -p 52-54
echo ""
echo "Thank you for your audit!"