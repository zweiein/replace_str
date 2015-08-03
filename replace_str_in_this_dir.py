#coding=UTF-8
import os, re, sys, codecs, time
'''
@功能:
    使用者指定 1.資料夾  2.想取代的字串  3.取代後的字串
    搜尋目錄下的所有scp檔，並修改
@使用方式：
    python replace_str_in_this_dir.py <target-dir> <target-str> <relplace-to-this-str>
'''

def ReadAndReplaceKeywords(file_name, target_str, replace_to_str):
    #print '@Rplacing scf files....'
    #print 'from  ' + file_name

    file2str = codecs.open(file_name, 'r', 'utf8').read()

    after_replaced_str = file2str.replace(target_str, replace_to_str)

    str2file = codecs.open(file_name, 'w', 'utf8')
    str2file.write(after_replaced_str)
#end ReadAndReplaceKeywords()



if __name__ == '__main__' :
    if len(sys.argv) != 4 :
        print 'Usage: python <python-file> ' \
              '<target-dir> <target-str> <relplace-to-this-str> '
    #end if
    else :
        #/Users/slp/Documents/kaldi/kaldi-trunk/egs/matbn/s0/mfcc_pitch
        cmd_find = '&&  find . -name \'*.scp\''
        scp_files = os.popen('cd ' + sys.argv[1] + cmd_find ).read()
        todo_scps = scp_files.split( )

        print '@Scanning scp files:'
        for scan_scp in todo_scps:
            print '  ' + scan_scp
        #end for

        for rep_scp in todo_scps:
            #sys.stdout.write('{0}\t{1}\r'.format('X', rep_scp))
            length = len(rep_scp)
            new_path = sys.argv[1] + rep_scp[1:length]
            ReadAndReplaceKeywords(new_path, sys.argv[2], sys.argv[3])
            #sys.stdout.flush()
            #time.sleep(0.5)
            #sys.stdout.write('{0}\t{1}\n'.format('O', rep_scp))
            #sys.stdout.flush()
            #time.sleep(0.1)
        #end for

        time.sleep(0.3)
        print '\n@Replacing scp files:'

        for i in range(20):
            sys.stdout.write('\r[{0}{1}]'.format('#'*i, ' '*(19-i)))
            sys.stdout.flush()
            time.sleep(0.05)
            if i == 19:
                sys.stdout.write(' 100%   success!\n\n')
        #end for
    #end else
