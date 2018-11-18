<?php
require_once 'auth.php';
require_once 'models.php';

$error = null;

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (!isset($_POST['username']) || strlen($_POST['username']) < 4) {
        $error = "Invalid username";
    }

    if (!isset($_POST['realname']) || strlen($_POST['realname']) < 2) {
        $error = "Invalid name";
    }

    if (!isset($_POST['password']) || strlen($_POST['password']) < 6) {
        $error = "Password too short";
    }

    if ($error === null) {
        $username = $_POST['username'];
        $realname = $_POST['realname'];
        $password = $_POST['password'];

        $u = User::register($username, $realname, $password);
        if ($u !== null) {
            set_user($u);
            header('Location: home.php');
            die();
        } else {
            $error = "Username already taken";
        }
    }
}

include 'header.php';
?>
        <div class="content">
            <h3>Register</h3>
            <?php if ($error !== null) { ?>
            <p class="error"><?php echo $error; ?></p>
            <?php } ?>
            <div class="login-form">
                <form action="register.php" method="post">
                    <input type="text" name="username" placeholder="Username" /><br/>
                    <input type="text" name="realname" placeholder="Real name" /><br/>
                    <input type="password" name="password" placeholder="Password" /><br/><br/>
                    <input type="submit" value="Register" />
                </form>
            </div>
        </div>
<?php
include 'footer.php';
?>
