
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.Select;

public class loginRobustnessTesting {
    public static void main(String[] args) throws InterruptedException {

		System.setProperty("webdriver.chrome.driver", "C:/Users/Ivan Tandyajaya/Documents/JavaSUTD/chromedriver_win32/chromedriver.exe");
		WebDriver driver = new ChromeDriver();
		driver.get("http://localhost:8000/");
//		driver.get("http://13.250.116.16:8000/");

		
		// maximize the browser window
		driver.manage().window().maximize();

		WebElement username = driver.findElement(By.name("username"));
		WebElement password = driver.findElement(By.name("password"));
		WebElement submit_button = driver.findElement(By.cssSelector("button[name='login']"));

		username.sendKeys("<script> alert('Fuzzed'); </script>");
		password.sendKeys("%$<1&<%+=!'83?+)9:++9138 42/ '7;0-,)06 '1(2;6>?99$%7!!*#96=>2&-/(5*)=$;0$$+;<12'?30&");
		Thread.sleep(500);
		submit_button.click();
		Thread.sleep(1500);

        WebElement username2 = driver.findElement(By.name("username"));
		WebElement password2 = driver.findElement(By.name("password"));
		WebElement submit_button2 = driver.findElement(By.cssSelector("button[name='login']"));

        username2.clear();
        username2.sendKeys("zskscocrxllosagkvaszlngpysurezehvcqcghygphnhonehczraznkibltfmocxddoxcmrvatcleysksodzlwmzdndoxrjfqigjhqjxkblyrtoaydlwwisrvxtxsejhfbnforvlfisojqaktcxpmjqsfsycisoexjctydzxzzutukdztxvdpqbjuqmsectwjvylvbixzfmqiabdnihqagsvlyxwxxconminadcaqjdzcnzfjlwccyudmdfceiepwvyggepjxoeqaqbjzvmjdlebxqvehkmlevoofjlilegieeihmetjappbisqgrjhglzgffqrdqcwfmmwqecxlqfpvgtvcddvmwkplmwadgiyckrfjddxnegvmxravaunzwhpfpyzuyyavwwtgykwfszasvlbwojetvcygectelwkputfczgsfsbclnkzzcjfywitooygjwqujseflqyvqgyzpvknddzemkegrjjrshbouqxcmixnqhgsgdwgzwzmgzfajymbcfezqxndbmzwnxjeevgtpjtcwgbzptozflrwvuopohbvpmpaifnyyfvbzzdsdlznusarkmmtazptbjbqdkrsnrpgdffemnpehoapiiudokczwrvpsonybfpaeyorrgjdmgvkvupdtkrequicexqkoikygepawmwsdcrhivoegynnhodfhryeqbebtbqnwhogdfrsrksntqjbocvislhgrgchkhpaiugpbdygwkhrtyniufabdnqhtnwreiascfvmuhettfpbowbjadfxnbtzhobnxsnf");
		password2.sendKeys("<script> alert('Fuzzed'); </script>");
		Thread.sleep(500);
		submit_button2.click();
		Thread.sleep(1500);

        WebElement username3 = driver.findElement(By.name("username"));
		WebElement password3 = driver.findElement(By.name("password"));
		WebElement submit_button3 = driver.findElement(By.cssSelector("button[name='login']"));
        
        username3.clear();
        username3.sendKeys("%$<1&<%+=!'83?+)9:++9138 42/ '7;0-,)06 '1(2;6>?99$%7!!*#96=>2&-/(5*)=$;0$$+;<12'?30&");
		password3.sendKeys("こんにちは");
		Thread.sleep(500);
		submit_button3.click();
		Thread.sleep(1500);

		
	}
}
