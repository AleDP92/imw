<!doctype html>
<html lang="es">
    <head>
        <meta charset="utf-8">
        <title>Table creator</title>
    </head>
    <body>
      <h1>Make your table</h1>
      <form action="cells.php" method="get">
          <label for="rows">Number of rows:</label>
          <input type="text" name="rows"/><br>
          <label for="cols">Number of columns:</label>
          <input type="text" name="cols"/><br>
          <input type="submit" value="enviar"/>
      </form>
    </body>
</html>