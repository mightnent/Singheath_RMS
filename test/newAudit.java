import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.Select;

public class newAudit {
	final static String admin_username = "admin";
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
        
        
        driver.get("http://13.250.116.16:8000/new-audit");
        Thread.sleep(1000);
        
        //Create new checklist
        Select selTenant = new Select(driver.findElement(By.className("tenants")));
        selTenant.selectByIndex(1);
        Select selChecklist = new Select(driver.findElement(By.name("checklist")));
        selChecklist.selectByIndex(1);
        Thread.sleep(1000);
        WebElement create_button = driver.findElement(By.cssSelector("button[id='b1']"));
        create_button.click();
        Thread.sleep(1000);
        
        //Fill up checklist
        //Q1 - pass
        WebElement comment1 = driver.findElement(By.name("comment"));
        comment1.sendKeys("good");
        Thread.sleep(1000);
        WebElement pass_button1 = driver.findElement(By.cssSelector("button[value='PASS']"));
        pass_button1.click();
        Thread.sleep(1000);
        
      //Q2 - fail
        WebElement comment2 = driver.findElement(By.name("comment"));
        comment2.sendKeys("bad");
        Thread.sleep(1000);
        WebElement pass_button2 = driver.findElement(By.cssSelector("button[value='FAIL']"));
        pass_button2.click();
        Thread.sleep(1000);
		
      //Q3 - NA
        WebElement comment3 = driver.findElement(By.name("comment"));
        comment3.sendKeys("N.A");
        Thread.sleep(1000);
        WebElement pass_button3 = driver.findElement(By.cssSelector("button[value='NA']"));
        pass_button3.click();
        Thread.sleep(1000);
        
        //Test previous and next button
        WebElement previousButton = driver.findElement(By.className("previous"));
        driver.navigate().to(previousButton.getAttribute("href"));
        Thread.sleep(1000);
        WebElement nextButton = driver.findElement(By.className("next"));
        driver.navigate().to(nextButton.getAttribute("href"));
        Thread.sleep(1000);
        WebElement doneButton = driver.findElement(By.className("done"));
        driver.navigate().to(doneButton.getAttribute("href"));
	}
}
