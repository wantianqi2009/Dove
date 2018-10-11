import os
import subprocess
import multiprocessing.pool
import glob

FILE_PATTERN = '*/*/*.in'

def find_locations(pattern=FILE_PATTERN):
    locations = []
    for input_path in glob.glob(pattern):
        cwd = os.path.dirname(input_path)
        input_file_name = os.path.basename(input_path)
        output_file_name = '%s.out'%(os.path.splitext(input_file_name)[0])
        error_file_name = '%s.err'%(os.path.splitext(input_file_name)[0])
        locations.append((
            cwd,
            input_file_name,
            output_file_name,
            error_file_name
        ))
    return locations
    
def execute(location):
    cwd, input_file_name, output_file_name, error_file_name = location
    print('Starting `%s` at `%s`...'%(input_file_name, cwd))
    with open(os.path.join(cwd, output_file_name), 'w') as out:
        with open(os.path.join(cwd, error_file_name), 'w') as err:
            process = subprocess.Popen([
                'ibrun',
                'pw.x', '-in', input_file_name
            ], stdout=out, stderr=err, cwd=cwd)
            process.communicate()
    print('Finished `%s`!'%(input_file_name))

if __name__ == '__main__':
    pool = multiprocessing.pool.Pool(6)
    pool.map(execute, find_locations())
    
