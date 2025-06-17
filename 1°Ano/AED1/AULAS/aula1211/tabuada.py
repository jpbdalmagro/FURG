with open('tabuada.html', 'w') as html:
    html.write("<!DOCTYPE html>\n<html>\n<head>\n")
    html.write("    <title>TABUADAS</title>\n")
    html.write("</head>\n<body>\n")
    for i in range(1, 11):
        html.write(f"   <h2> Tabuada do {i}:</h2>\n")
        html.write("    <table border=1>\n")
        for n in range(11):
            html.write(f"      <tr><td>{i} x {n} = </td><td>{i * n}</td></tr>\n")
        html.write("    </table>\n")
    html.write("</body>\n</html>")
        