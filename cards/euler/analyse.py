import json
import os
import glob

def get_all_solutions():
	files = glob.glob('/tmp/solutions/project_euler/*', recursive=True)
	#return [f for f in files if f[-4:] != '.txt' and f[-4:] != '.csv'] # remove a few data files
	return files


if __name__ == '__main__':	
	solution_files = get_all_solutions()
	num_problems = len(solution_files)
	data = {"num_problems": num_problems}
	with open('/tmp/cloc.csv', 'r') as filereader:
		csv = filereader.read()
		print(csv)
		curr_lang = 0
		total_files = 0
		langs = {}
		for lang in csv.split('\n')[1:]:
			parts = lang.split(',')
			if len(parts) == 1:
				break
			print(parts)
			langs[parts[1]] = int(parts[0])

		for lang in sorted(langs, key=lambda x:langs[x], reverse=True):
			data['lang%d' % curr_lang] = lang
			num_files = langs[lang]
			data['num_lang%d' % curr_lang] = num_files
			total_files += num_files
			curr_lang += 1
		data['num_solutions'] = total_files

	json_data = json.dumps(data, indent=4)
	with open('data.json', 'w') as filewriter:
		filewriter.write(json_data)
		filewriter.write('\n')
	
	
