<?php
require_once 'auth.php';
require_once 'models.php';

$error = null;

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['username']) && isset($_POST['password'])) {
    $username = $_POST['username'];
    $password = $_POST['password'];

    $u = User::login($username, $password);
    if ($u !== null) {
        set_user($u);
        header('Location: home.php');
        die();
    } else {
        $error = 'Invalid username or password.';
    }
}

include 'header.php';
?>
        <div class="content">
            <h3>Login</h3>
<?php if ($error !== null) { ?>
            <p class="error"><?php echo $error; ?></p>
<?php } ?>
            <div class="login-form">
                <form action="login.php" method="post">
                    <input type="text" name="username" placeholder="Username" /><br/>
                    <input type="password" name="password" placeholder="Password" /><br/><br/>
                    <input type="submit" value="Login" />
                </form>
                <a href="register.php">Register</a>
            </div>
        </div>
<?php
include 'footer.php';
?>
