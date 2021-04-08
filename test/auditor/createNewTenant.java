import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class createNewTenant {
    final static String admin_password = "password1.1";
    static String auditor_user = "testAuditor1";
		
	public static void main(String[] args) throws InterruptedException {		

		System.setProperty("webdriver.chrome.driver","D:/Joon Kang/chromedriver.exe");
		WebDriver driver = new ChromeDriver();
//		driver.get("http://localhost:8000/");
        driver.get("http://13.250.116.16:8000/");
		
        WebElement username = driver.findElement(By.name("username"));
        WebElement password = driver.findElement(By.name("password"));
        WebElement submit_button = driver.findElement(By.cssSelector("button[name='login']"));

        username.sendKeys(auditor_user);
        password.sendKeys(admin_password);
        submit_button.click();
        
        
        driver.get("http://13.250.116.16:8000/manage-tenant");
        Thread.sleep(1000);
        

        // Fill up new tenant details
        WebElement compName = driver.findElement(By.name("business_name"));
        compName.sendKeys("KFC");
        Thread.sleep(500);
        WebElement ownerName = driver.findElement(By.name("name"));
        ownerName.sendKeys("Bob");
        Thread.sleep(500);
        WebElement uen = driver.findElement(By.name("uen"));
        uen.sendKeys("Z48856958");
        Thread.sleep(500);
        WebElement contact = driver.findElement(By.name("contact"));
        contact.sendKeys("83655952");
        Thread.sleep(500);
        WebElement email = driver.findElement(By.name("email"));
        email.sendKeys("bob@kfc.com");
        Thread.sleep(500);
        WebElement leaseDate = driver.findElement(By.name("lease_end_date"));
        leaseDate.sendKeys("02062023");
        Thread.sleep(500);
//        WebElement create_button = driver.findElement(By.cssSelector("button[id='b1']"));
//        create_button.click();
        driver.findElement(By.name("lease_end_date")).submit();
	}
}