#include <iostream>
#include <fstream>

using namespace std;

int count_increases(char *mem, int size)
{
	int old_num = 0;
	int new_num = 0;
	int increases = 0;
	int i = 0;
	
	while (mem[i] != '\n')
	{
		old_num = old_num * 10 + mem[i] - '0';
		i++;
	}
	while (i < size)
	{
		new_num = 0;
		while (mem[i] != '\n' && i < size)
		{
			new_num = new_num * 10 + mem[i] - '0';
			i++;
		}
		i++;
		if (new_num > old_num)
			increases++;
		old_num = new_num;
	}
	return increases;
}

int	main() 
{
	fstream file;
	streampos pos;
	int size;
	char *mem;

	file.open("input.txt");
	if (file.is_open())
	{
		file.seekg (0, ios::end);
		pos = file.tellg();
		size = (int)(pos) + 1;
		mem = new char [size];
		mem[size - 1] = '\0';

		file.seekg (0, ios::beg);
		file.read (mem, size);
		file.close();
	}
	else
		cout << "File didn't open\n";

	cout << count_increases(mem, size) << "\n";
	return 0;
}
