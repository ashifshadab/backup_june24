package com.test;


import java.io.Serializable;
import java.util.Map;

public class DelayedSettlementVO extends CommonVo implements Serializable{

	
	private static final long serialVersionUID = 1L;
	private  String comments = "";
	private  String branch = "";
	private  String fundDescription = "";
	private  String gtid = "";
	private  String valueDate = "";
	private  String currency = "";
	private  double interest = 0;
	private  String fee = "";
	private  String dividend = "";
	private  String netAmount = "";
	private  String wireId = "";
	private  String wireValueDate = "";
	private  String wireAmount = "";
	private  String delay = "";
	private  String cpty = "";
	private  String cashAccount = "";
	private  String client = "";
	private  String clientID = "";
	private  String tradeType = "";
	private  String folder = "";
	private  String investmentId = "";
	private  String securityDescription = "";
	private  String fundId = "";
	private  String paymentTypeCode = "";
		 		 				 											

	
	

	public DelayedSettlementVO() {
		super();
	}

	public DelayedSettlementVO(String comments, String branch, String fundDescription, String gtid,
			String valueDate, String currency, double interest, String fee, String dividend, String netAmount,
			String wireId, String wireValueDate, String wireAmount, String delay, String cpty, String cashAccount,
			String client, String clientID, String tradeType, String folder, String investmentId,
			String securityDescription, String fundId, String paymentTypeCode) {
		super();
		this.comments = comments;
		this.branch = branch;
		this.fundDescription = fundDescription;
		this.gtid = gtid;
		this.valueDate = valueDate;
		this.currency = currency;
		this.interest = interest;
		this.fee = fee;
		this.dividend = dividend;
		this.netAmount = netAmount;
		this.wireId = wireId;
		this.wireValueDate = wireValueDate;
		this.wireAmount = wireAmount;
		this.delay = delay;
		this.cpty = cpty;
		this.cashAccount = cashAccount;
		this.client = client;
		this.clientID = clientID;
		this.tradeType = tradeType;
		this.folder = folder;
		this.investmentId = investmentId;
		this.securityDescription = securityDescription;
		this.fundId = fundId;
		this.paymentTypeCode = paymentTypeCode;
	}

	@Override
	public boolean isValidObject() {
		// TODO Auto-generated method stub
		return false;
	}



	@Override
	public Map<String, Object> getData() {
		// TODO Auto-generated method stub
		return null;
	}



	@Override
	public String getStatus() {
		// TODO Auto-generated method stub
		return null;
	}



	@Override
	public void setStatus(String status) {
		// TODO Auto-generated method stub
		
	}

	public String getComments() {
		return comments;
	}



	public void setComments(String comments) {
		if(comments == null)
			this.comments = "";
		else
			this.comments = comments;
	}



	public String getBranch() {
		return branch;
	}



	public void setBranch(String branch) {
		if(branch == null)
			this.branch = "";
		else
			this.branch = branch;
	}



	public String getFundDescription() {
		return fundDescription;
	}



	public void setFundDescription(String fundDescription) {
		if(fundDescription == null)
			this.fundDescription = "";
		else
			this.fundDescription = fundDescription;
	}



	public String getGtid() {
		return gtid;
	}



	public void setGtid(String gtid) {
		if(gtid == null)
			this.gtid = "";
		else
			this.gtid = gtid;
	}



	public String getValueDate() {
		return valueDate;
	}



	public void setValueDate(String valueDate) {
		if(valueDate == null)
			this.valueDate = "";
		else
			this.valueDate = valueDate;
	}



	public String getCurrency() {
		return currency;
	}



	public void setCurrency(String currency) {
		if(currency == null)
			this.currency = "";
		else
			this.currency = currency;
	}



	public double getInterest() {
		return interest;
	}



	public void setInterest(double interest) {
		this.interest = interest;
	}



	public String getFee() {
		return fee;
	}



	public void setFee(String fee) {
		if(fee == null)
			this.fee = "";
		else
			this.fee = fee;
	}



	public String getDividend() {
		return dividend;
	}



	public void setDividend(String dividend) {
		if(dividend == null)
			this.dividend = "";
		else
			this.dividend = dividend;
	}



	public String getNetAmount() {
		return netAmount;
	}



	public void setNetAmount(String netAmount) {
		if(netAmount == null)
			this.netAmount = "";
		else
			this.netAmount = netAmount;
	}



	public String getWireId() {
		return wireId;
	}



	public void setWireId(String wireId) {
		if(wireId == null)
			this.wireId = "";
		else
			this.wireId = wireId;
	}



	public String getWireValueDate() {
		return wireValueDate;
	}



	public void setWireValueDate(String wireValueDate) {
		if(wireValueDate == null)
			this.wireValueDate = "";
		else
			this.wireValueDate = wireValueDate;
	}



	public String getWireAmount() {
		return wireAmount;
	}



	public void setWireAmount(String wireAmount) {
		if(wireAmount == null)
			this.wireAmount = "";
		else
			this.wireAmount = wireAmount;
	}



	public String getDelay() {
		return delay;
	}



	public void setDelay(String delay) {
		if(delay == null)
			this.delay = "";
		else
			this.delay = delay;
	}



	public String getCpty() {
		return cpty;
	}



	public void setCpty(String cpty) {
		if(cpty == null)
			this.cpty = "";
		else
			this.cpty = cpty;
	}



	public String getCashAccount() {
		return cashAccount;
	}



	public void setCashAccount(String cashAccount) {
		if(cashAccount == null)
			this.cashAccount = "";
		else
			this.cashAccount = cashAccount;
	}



	public String getClient() {
		return client;
	}



	public void setClient(String client) {
		if(client == null)
			this.client = "";
		else
			this.client = client;
	}



	public String getClientID() {
		return clientID;
	}



	public void setClientID(String clientID) {
		if(clientID == null)
			this.clientID = "";
		else
			this.clientID = clientID;
	}



	public String getTradeType() {
		return tradeType;
	}



	public void setTradeType(String tradeType) {
		if(tradeType == null)
			this.tradeType = "";
		else
			this.tradeType = tradeType;
	}



	public String getFolder() {
		return folder;
	}



	public void setFolder(String folder) {
		if(folder == null)
			this.folder = "";
		else
			this.folder = folder;
	}



	public String getInvestmentId() {
		return investmentId;
	}



	public void setInvestmentId(String investmentId) {
		if(investmentId == null)
			this.investmentId = "";
		else
			this.investmentId = investmentId;
	}



	public String getSecurityDescription() {
		return securityDescription;
	}



	public void setSecurityDescription(String securityDescription) {
		if(securityDescription == null)
			this.securityDescription = "";
		else
			this.securityDescription = securityDescription;
	}

	public String getFundId() {
		return fundId;
	}

	public void setFundId(String fundId) {
		if(fundId == null)
			this.fundId = "";
		else
			this.fundId = fundId;
	}

	
	public String getPaymentTypeCode() {
		return paymentTypeCode;
	}

	public void setPaymentTypeCode(String paymentTypeCode) {
		
		if(paymentTypeCode == null)
			this.paymentTypeCode = "";
		else
			this.paymentTypeCode = paymentTypeCode;
	}


	@Override
	public String toString() {
		String returnString ="";
		
		/*returnString = "  comments				"+this.comments 
				+ "  branch					"+this.branch 			
				+ "  fundDescription		"+this.fundDescription 
				+ "  paymentTypeCode        "+this.paymentTypeCode
				+ "  gtid					"+this.gtid 				
				+ "  valueDate				"+this.valueDate 			
				+ "  currency				"+this.currency 			
				+ "  interest				"+this.interest 			
				+ "  fee					"+this.fee 				
				+ "  dividend				"+this.dividend 			
				+ "  netAmount				"+this.netAmount 			
				+ "  wireId					"+this.wireId 			
				+ "  wireValueDate			"+this.wireValueDate 		
				+ "  wireAmount				"+this.wireAmount 		
				+ "  delay					"+this.delay 				
				+ "  cpty					"+this.cpty 				
				+ "  cashAccount			"+this.cashAccount 		
				+ "  client					"+this.client 			
				+ "  clientID				"+this.clientID 			
				+ "  tradeType				"+this.tradeType 			
				+ "  folder					"+this.folder 			
				+ "  investmentId			"+this.investmentId 		
					+ "  securityDescription	"+this.securityDescription
				+ "  fundId					"+this.fundId ;*/
		
		returnString = this.comments 
				+ ":"+this.branch 			
				+ ":"+this.fundDescription 
				+ ":"+this.paymentTypeCode
				+ ":"+this.gtid 				
				+ ":"+this.valueDate 			
				+ ":"+this.currency 			
				+ ":"+this.interest 			
				+ ":"+this.fee 				
				+ ":"+this.dividend 			
				+ ":"+this.netAmount 			
				+ ":"+this.wireId 			
				+ ":"+this.wireValueDate 		
				+ ":"+this.wireAmount 		
				+ ":"+this.delay 				
				+ ":"+this.cpty 				
				+ ":"+this.cashAccount 		
				+ ":"+this.client 			
				+ ":"+this.clientID 			
				+ ":"+this.tradeType 			
				+ ":"+this.folder 			
				+ ":"+this.investmentId 		
				+ ":"+this.securityDescription
				+ ":"+this.fundId ;
		
		
		return returnString;}	

	
}
