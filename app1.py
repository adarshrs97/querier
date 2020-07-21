import re
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', type=str)
    b = request.args.get('b', type=str)
    f = patern_subsq(a,b)
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
    app.run(host='0.0.0.0',port=5663, debug=True)

