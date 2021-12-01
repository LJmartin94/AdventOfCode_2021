#include <iostream>
#include <fstream>

using namespace std;

int	main() 
{
	fstream file;
	streampos size;
	char *mem;

	file.open("input.txt");
	if (file.is_open())
	{
		file.seekg (0, ios::end);
		size = file.tellg();
		mem = new char [size];

		file.seekg (0, ios::beg);
		file.read (mem, size);
		file.close();
	}
	else
		cout << "File didn't open\n";
	cout<< mem;
	return 0;
}
