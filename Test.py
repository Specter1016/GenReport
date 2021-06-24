import os
import time
import requests


def newReadVersion():

    with open('DataFile/cpu/Dashboards - vRealize Operations Manager.html','r',encoding="utf-8") as read_cpu:

        with open('ValueReport.text','w') as setNewData:

            with open('Royalcpu.text', 'w') as setNewcpu:

                with open('Royalram.text', 'w') as setNewram:

                    with open('Royalnet.text', 'w') as setNewnet:

                        get_cpu = read_cpu.readlines();


                        count=0;
                        setsettt = 0;
                        get_cpu_step3 = "";
                        countstate = 0;

                        opencpu = [];
                        openram = [];
                        opennet = [];

                        for x in get_cpu:

                            if '<b>H:</b> ' in x:

                                    get_cpu_step2 = x.split('<b>H:</b>');
                                    print(len(get_cpu_step2));

                                    for y in get_cpu_step2:


                                        if setsettt == 0:

                                            setsettt = setsettt+1;

                                        else:

                                            for z in y :

                                                if z != '<' and count == 0:

                                                    count =count +1;

                                                if z !=[] and z != '<' and count !=0:

                                                    get_cpu_step3 = get_cpu_step3+str(z);


                                                else:

                                                    if countstate <= 10:

                                                        setNewcpu.writelines(format(get_cpu_step3).strip());
                                                        setNewcpu.writelines('\n');
                                                        get_cpu_step3="";
                                                        countstate = countstate+1;
                                                        break;

                                                    if countstate <= 21:

                                                        setNewram.writelines(format(get_cpu_step3).strip());
                                                        setNewram.writelines('\n');
                                                        get_cpu_step3 = "";
                                                        countstate = countstate + 1;
                                                        break;

                                                    if countstate <= 32:
                                                        setNewnet.writelines(format(get_cpu_step3).strip());
                                                        setNewnet.writelines('\n');
                                                        get_cpu_step3 = "";
                                                        countstate = countstate + 1;
                                                        break;





setplayload = list();

with open('ValueReport.text','r',encoding='utf-8') as getreporttext:
    p = '';
    for x in getreporttext:

        if 'span' in x:
            for y in x:
                if '/' in y:
                    setplayload.append(p.strip())
                    p = '';
                    break;
                else:
                    p = p + y;
        else:
            setplayload.append(x.strip());

    print(len(setplayload))
