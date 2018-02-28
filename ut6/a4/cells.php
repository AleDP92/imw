<!doctype html>
<html lang="es">
    <head>
        <meta charset="utf-8">
        <title>Probando PHP!!</title>
    </head>
    <body>
        <?php
         
            if (isset($_GET["rows"]) and isset($_GET["cols"])) {
                $rows = (int)$_GET["rows"];
                $cols = (int)$_GET["cols"];
                if ($rows < 1 or $cols < 1) {
                  echo("<p style='color:red;'>You have to specify a number of rows and a number of columns</p>");
                }
            else {
                echo("<table border='1'>");
                  for($i=1; $i<=$rows; $i++){
                    echo("<tr>");
                for($j=1; $j<=$cols; $j++){
                    echo("<td>$i-$j</td>");
                    }
                    echo("</tr>");
                  }
                  echo("</table>");
                }
            }
        ?>
    </body>
</html>