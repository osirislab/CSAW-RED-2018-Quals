<?php
    class DB {

        private static function initDBConnnection() {
            $SQL_HOST = "localhost";
            $SQL_PORT = 3306;
            $SQL_USER = "ola";
            $SQL_PASS = "ola";
            $SQL_DB = "ola";

            try {
                $con = new PDO("mysql:host=$SQL_HOST;port=$SQL_PORT;dbname=$SQL_DB", $SQL_USER, $SQL_PASS);

                return $con;
            } catch (PDOException $e) {
                die("Error establishing database connection.");
            }
        }

        public static function queryDB($preparedQuery, $params, $numReturnRows = -1) {
            $rows = array();
            $con = DB::initDBConnnection();

            $stmt = $con->prepare($preparedQuery);

            if (is_array($params)) {
                foreach ($params as $placeholder => $value) {
                    $stmt->bindValue($placeholder, $value);
                }
            }

            if ($stmt->execute()) {
                if ($numReturnRows != -1) {
                    for ($i = 0; $i < $numReturnRows; $i++) {
                        if ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
                            $rows[] = $row;
                        }
                    }

                } else {
                    while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
                        $rows[] = $row;
                    }
                }

                if ($numReturnRows != 0) {
                    return $rows;
                } else {
                    return $con->lastInsertId();
                }
            } else {
                return false;
            }
        }
    }
