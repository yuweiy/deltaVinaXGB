import os
import sys
import errno
import distutils.spawn
import DXGB.path_const as pc


def get_tool(name):
    executable = distutils.spawn.find_executable(name)
    if executable:
        return executable
    else:
        try:
            tool = eval('pc.' + name.split('.')[0].upper())
        except:
            tool = None
            raise ValueError('Cannot find ' + name)
    return tool

def convert_format(fname, fname_type, outname,outname_type,delH=False):
    '''
    use obabel to convert structure file format
    :param fname: file name
    :param fname_type: file type
    :param outname: output file name
    :param outname_type: output file format
    :return:
    '''
    #print(not get_tool('test'))
    if not get_tool('obabel'):
        print('obabel is not found!')
        sys.exit()

     
    f = open(outname,'w')
    if delH == False:
        subprocess.Popen(['obabel','-i'+fname_type, fname, '-o' + outname_type], stdout=f).communicate()
    else:
        subprocess.Popen (['obabel', '-d','-i' + fname_type, fname, '-o' + outname_type], stdout=f).communicate ( )
    f.close()


def format_convert_to_temp(fname,in_format,out_format):
    '''
    Generate temp file and store the converted format in temp file  
    '''
    temp = tempfile.NamedTemporaryFile(delete=False)
        
    convert_format(fname,in_format,temp.name, out_format)
    return temp.name

def get_inputtype(input):
    """
    Get input types based on input file format
    
    :param input:input file
    :return: type 

    """
    type = "Wrong Type"
    if input.split("/")[-1].split(".")[-1] == "mol2":
        type = "mol2"
    elif input.split("/")[-1].split(".")[-1] == "pdb":
        type = "pdb"
    elif input.split("/")[-1].split(".")[-1] == "sdf":
        type = "sdf"
    elif input.split("/")[-1].split(".")[-1] == "smi":
        type = "smile"
    print("Input Type:" +type)

    return type