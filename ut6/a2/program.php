<!doctype html>
<html lang="es">
    <head>
        <meta charset="utf-8">
        <title>Probando PHP!!</title>
    </head>
    <body>
        <?php
            $name = $_POST["name"];
            $surname = $_POST["surname"];
            $salary = (float)$_POST["salary"];
            $age = (int)$_POST["age"];

            if ($salary > 2000) {
            echo("$salary");
        }
            else if ($salary > 1000 and $salary < 2000) {
                if ($age > 45) {
                    $op1 = $salary * 1.03;
                    echo("$op1");
            }
                else {
                    $op2 = $salary * 1.10;
                    echo("$op2");
            }
        }
            else {
                if ($age < 30) {
                    echo("1100");
            }
                else if ($age > 30 and $age < 45) {
                    $op3 = $salary * 1.03;
                    echo("$op3");
            }
                else {
                    $op4 = $salary * 1.15;
                    echo("$op4");
            }
        }
        ?>
    </body>
</html>