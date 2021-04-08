import org.openqa.selenium.By;
import org.openqa.selenium.StaleElementReferenceException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

public class clickAllLink {
	final static String admin_username = "admin";
    final static String admin_password = "password1.1";
    static String auditor_user = "testAuditor1";
		
	public static void main(String[] args) throws InterruptedException {		

		System.setProperty("webdriver.chrome.driver","D:/Joon Kang/chromedriver.exe");
		WebDriver driver = new ChromeDriver();
		driver.get("http://localhost:8000/");
//        driver.get("http://13.250.116.16:8000/");
		
        WebElement username = driver.findElement(By.name("username"));
        WebElement password = driver.findElement(By.name("password"));
        WebElement submit_button = driver.findElement(By.cssSelector("button[name='login']"));

        username.sendKeys(auditor_user);
        password.sendKeys(admin_password);
        submit_button.click();
        
		// get all the links
		java.util.List<WebElement> links = driver.findElements(By.tagName("a"));

		// print all the links
		for (int i = 0; i < links.size(); i=i+1) {
			System.out.println(i + " " + links.get(i).getText());
			System.out.println(i + " " + links.get(i).getAttribute("href"));
		}
		
		// click all links in a web page
		for(int i = 0; i < links.size(); i++)
		{
			System.out.println("*** Navigating to" + " " + links.get(i).getAttribute("href"));
			if (links.get(i).getAttribute("href") == null) {
				continue;
			}
			boolean staleElementLoaded = true;
			//the loop checks whether the elements is properly loaded
			while(staleElementLoaded) {
				try {
					//navigate to the link
					driver.navigate().to(links.get(i).getAttribute("href"));
					Thread.sleep(3000);
					//click the back button in browser
					driver.navigate().back();
					links = driver.findElements(By.tagName("a"));
					System.out.println("*** Navigated to" + " " + links.get(i).getAttribute("href"));
					staleElementLoaded = false;
				} catch (StaleElementReferenceException e) {
					staleElementLoaded = true;
				}
			}
		}
	}
}