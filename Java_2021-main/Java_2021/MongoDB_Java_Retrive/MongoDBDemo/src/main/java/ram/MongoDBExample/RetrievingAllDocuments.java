package ram.MongoDBExample;

import java.util.Iterator;

import org.bson.Document;

import com.mongodb.MongoClient;
import com.mongodb.client.FindIterable;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;

public class RetrievingAllDocuments
{

	public static void main(String[] args)
	{
		// Creating a Mongo client
		try (MongoClient mongoClient = new MongoClient("localhost", 27017))
		{
			// Accessing the order database
			MongoDatabase orderDatabase = mongoClient.getDatabase("order");
			System.out.println("Database Name = " + orderDatabase.getName());

			// Retrieving a product collection
			MongoCollection<Document> productCollection = orderDatabase.getCollection("product");
			System.out.println("product Collection selected successfully");

			// Getting the iterable object
			FindIterable<Document> findIterable = productCollection.find();
			// Getting the iterator
			Iterator<Document> iterator = findIterable.iterator();
			while (iterator.hasNext())
			{
				Document document = iterator.next();
				System.out.println(document);
				System.out.println("Product Name = " + document.get("productName"));
			}
		}
		catch (Exception exe)
		{
			exe.printStackTrace();
		}
	}
}
