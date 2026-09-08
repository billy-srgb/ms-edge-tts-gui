import unittest

from tts_engine import (
    _ssl_context,
    build_sentence_timeline,
    is_ssl_cert_error,
)


class TimelineTests(unittest.TestCase):
    def test_builds_timeline_directly_from_sentence_boundaries(self):
        payload = build_sentence_timeline(
            [
                {
                    "text": "First sentence.",
                    "offset": 500000,
                    "duration": 12500000,
                },
                {
                    "text": "Second sentence!",
                    "offset": 13000000,
                    "duration": 20000000,
                },
            ],
            "en-US-AndrewMultilingualNeural",
            "+0%",
        )

        self.assertEqual(payload["boundary"], "SentenceBoundary")
        self.assertEqual(payload["sentences"][0]["start"], 0.05)
        self.assertEqual(payload["sentences"][0]["end"], 1.3)
        self.assertEqual(payload["sentences"][1]["start"], 1.3)
        self.assertEqual(payload["sentences"][1]["end"], 3.3)
        self.assertEqual(payload["sentences"][1]["text"], "Second sentence!")

    def test_rejects_invalid_sentence_boundary(self):
        with self.assertRaises(RuntimeError):
            build_sentence_timeline(
                [{"text": "Missing duration.", "offset": 500000}],
                "en-US-AndrewMultilingualNeural",
                "+0%",
            )


class SslBundleTests(unittest.TestCase):
    def test_ssl_context_loads_certifi_cas(self):
        context = _ssl_context()
        self.assertGreater(len(context.get_ca_certs()), 0)

    def test_detects_certificate_verify_failed(self):
        self.assertTrue(
            is_ssl_cert_error(
                "SSLCertVerificationError: certificate verify failed: "
                "unable to get local issuer certificate"
            )
        )
        self.assertFalse(is_ssl_cert_error("connection timed out"))


if __name__ == "__main__":
    unittest.main()
