

import org.junit.After;
import org.junit.Before;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import org.junit.Test;

import java.util.List;

import static org.junit.Assert.*;

public class TestUserAdminFunctions {
    final String admin_username = "admin";
    final String admin_password = "password1.1";
    String auditor_user = "testAuditor1";
    String tenant_user = "testTenant1";
    WebDriver driver;

    @Before
    public void createDriver() {
        System.setProperty("webdriver.gecko.driver", "C:\\Users\\Heriuma\\AndroidStudioProjects\\geckodriver.exe\\");
        driver = new FirefoxDriver();

        driver.get("http://13.250.116.16:8000/");
        // maximize the browser window
        driver.manage().window().maximize();
    }

    public void logInAsAdmin() {
        logOut();
        driver.get("http://13.250.116.16:8000/login");
        WebElement username = driver.findElement(By.id("id_username"));
        WebElement password = driver.findElement(By.id("id_password"));
        WebElement submit_button = driver.findElement(By.cssSelector("button[name='login']"));

        username.sendKeys(admin_username);
        password.sendKeys(admin_password);
        submit_button.click();
    }

    public void logInAsAuditor() {
        logOut();
        driver.get("http://13.250.116.16:8000/login");
        WebElement username = driver.findElement(By.id("id_username"));
        WebElement password = driver.findElement(By.id("id_password"));
        WebElement submit_button = driver.findElement(By.cssSelector("button[name='login']"));

        username.sendKeys(auditor_user);
        password.sendKeys(admin_password);
        submit_button.click();
    }

    private void logOut() {
        driver.get("http://13.250.116.16:8000/logout");
    }


    private void logInAsNormalUser(String pw) {
        logOut();
        driver.get("http://13.250.116.16:8000/login");
        WebElement username = driver.findElement(By.id("id_username"));
        WebElement password = driver.findElement(By.id("id_password"));
        WebElement submit_button = driver.findElement(By.cssSelector("button[name='login']"));

        username.sendKeys(tenant_user);
        if (pw == null) {
            password.sendKeys(admin_password);
        } else {
            password.sendKeys(pw);
        }
        submit_button.click();
    }

    private void nav_to_users_table() {
        List<WebElement> elements = driver.findElements(By.cssSelector("th > a"));
        for (WebElement a : elements) {
            if (a.getText().equals("Users")) {
                a.click();
                break;
            }
        }
    }

    @Test
    public void testAdminLogin() {
        try {
            logInAsAdmin();

            assertNotNull(driver.findElement(By.cssSelector("a[href='/admin/auth/user/add/']")));
            assertEquals(driver.findElement(By.id("site-name")).getText(), "SingHealth RMS Admin");

            Thread.sleep(1000);

            // add user
            logInAsAuditor();
            driver.get("http://13.250.116.16:8000/manage-tenant");
            WebElement form = driver.findElement(By.cssSelector("form[action='/create-tenant']"));
            assertNotNull(form);
            List<WebElement> elements = driver.findElements(By.cssSelector("form[action='/create-tenant'] input"));
            for (WebElement a : elements) {
                if (a.getAttribute("type").equals("date")) {
                    a.sendKeys("2022-12-20");
                } else if (a.getAttribute("type").equals("text")) {
                    a.sendKeys("testAccountCreation");
                }
            }
            WebElement button = driver.findElement(By.cssSelector("button#b1"));
            button.click();

            Thread.sleep(3000);
            logInAsAdmin();
            nav_to_users_table();
            elements = driver.findElements(By.cssSelector("th.field-username > a"));
            for (WebElement a : elements) {
                if (a.getText().equals("testAccountCreation")) {
                    assertTrue(true);
                    return;
                }
            }
            assertTrue(false);
        }
        catch (InterruptedException e) {
            System.out.println("execution interrupted");
        }

    }
}