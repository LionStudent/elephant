import covid19

import json

...


@app.route('/sendSinglePost', methods=['POST'])

def sendSinglePost():

    response = {}

    if request.method == 'POST':

        options = json.loads(request.data)

        filename = covid19.getImageFilename(options)

        options['url'] = store.addImageData(filename)

        store.addTextData(options)

    return jsonify(options)