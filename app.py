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

if __name__ == '__main__':
    app.run(port=5662, debug=True)

