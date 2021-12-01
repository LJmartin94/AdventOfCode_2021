#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int count_increases(char *mem, int size)
{
	int new_num = 0;
	int increases = 0;
	int i = 0;
	int j = 0;
	int single_array[2000];
	int sum_array[1998];
	vector<int> naampje;
	
	// turn input into array of integers
	while (i < size)
	{
		new_num = 0;
		while (mem[i] != '\n' && i < size)
		{
			new_num = new_num * 10 + mem[i] - '0';
			i++;
		}
		i++;
		single_array[j] = new_num;
		j++;
	}
	//null sum_array
	j = 0;
	while (j < 1998)
	{
		sum_array[j] = 0;
		j++;
	}
	//make sum_array
	i = 0;
	j = 0;
	while(i < 2000)
	{
		if (j - 2 >= 0 && j < 2000)
			sum_array[j - 2] = sum_array[j - 2] + single_array[i];
		if (j - 1 >= 0 && j < 1999)
			sum_array[j - 1] = sum_array[j - 1] + single_array[i];
		if (j == i && j < 1998)
			sum_array[j] = sum_array[j] + single_array[i];
		i++;
		j++;
	}
	//compare sum_array
	j = 0;
	while (j < 1998)
	{
		if (j - 1 >= 0 && sum_array[j - 1] < sum_array[j])
			increases++;
		j++;
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
