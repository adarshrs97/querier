import re
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', type=str)
    b = request.args.get('b', type=str)
    op = querycomb(a,b)
    return jsonify(result=op)
# """Add two numbers server side, ridiculous but well..."""

def querycomb(query,replacement):
    file_object = open('qbout.txt', 'a')
    variable = '@'
    # replacement = 'ga_barrow,ga_ben hill,ga_calhoun,ga_carroll,ga_chattahoochee,ga_chattooga,ga_dodge,ga_echols,ga_elbert,ga_floyd,ga_franklin,ga_heard,ga_irwin,ga_jasper,ga_jeff davis,ga_jenkins,ga_lanier,ga_laurens,ga_liberty,ga_long,ga_macon,ga_mcintosh,ga_miller,ga_mitchell,ga_montgomery,ga_morgan,ga_oglethorpe,ga_peach,ga_pike,ga_pulaski,ga_randolph,ga_seminole,ga_stewart,ga_taliaferro,ga_telfair,ga_terrell,ga_tift,ga_towns,ga_treutlen,ga_upson,ga_warren,ga_webster,ga_wheeler,ga_wilcox,ga_wilkes,ga_wilkinson,ga_worth'
    listrep = replacement.split(",")
    # query = "update @.building set bath_source_stnd_code = null where total_calculated_bath_count is null and bath_source_stnd_code is not null;"
    # xint = len(listrep)
    for i in range(len(listrep)):
        j = i-1
        rstring = ""+listrep[j]+""
        # print rstring
        qbo = query.replace(variable,rstring)
        file_object.write(qbo+'\n')
    file_op = open('qbout.txt', 'r')
    opc = file_op.read()
    file_t = open('qbout.txt', 'r+')
    file_t.truncate(0)
    file_object.close()
    return opc
    
    # open('qbout.txt', 'w').close()
@app.route('/_formatsub')
def formatsub():
    q = request.args.get('a', type=str)
    w = request.args.get('b', type=str)
    f = patern_subsq(q,w)
    return jsonify(result=f)
def patern_subsq(text,unf):
	idx = []
	sidx = []
	subsq = []
	sum = 0
	pattern = 'x+'
	if text[:1] != 'x':
		output_query = 'err'

	else :

		output_query = 'concat('

		def remove_values_from_list(the_list, val):
			return [value for value in the_list if value != val]

		for match in re.finditer(pattern, text):
			s = match.start()
			e = match.end()
			f = e-s
			idx.append(f)
			# print(s,e,f)

		for i in range(len(idx)-1):
			sum = sum + idx[i] + 1
			sidx.append(sum)
		# print sidx

		for i in range(len(idx)):
			if i == 0:
				sq = "substring(1,"+str(idx[i])+")"
				subsq.append(sq)
			else:
				sq = "substring("+str(sidx[i-1]-i+1)+","+str(idx[i])+")"
				subsq.append(sq)

		# print subsq

		sep = re.sub('x+','x',text)
		# print sep
		sepidx = sep.split('x')
		sepidxout = remove_values_from_list(sepidx,'')
		# print sepidxout

		for n in range(len(sepidxout)):
			sout = ""+subsq[n]+",'"+sepidxout[n]+"',"
			output_query = output_query + sout
			# print sout
		if range(len(subsq)) != range(len(sepidxout)):
			output_query = output_query + subsq[len(subsq)-1] + ")"
		else:
			output_queryp = output_query + ")"
			output_query = output_queryp.replace(',)',')')
	final_output=output_query.replace('substring(','substring('+unf+',')
	return final_output
# unfp = 'uapn'
# reqf = 'x-xx-xx-xx-xxx-xxxx-xxxx'
# print patern_subsq(reqf,unfp)



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5662, debug=True)

